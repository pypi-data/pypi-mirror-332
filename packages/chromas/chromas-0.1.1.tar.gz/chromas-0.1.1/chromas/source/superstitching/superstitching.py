"""
superstitch.py

This script implements "superstitch", a tool for long-term chromatophore tracking
across multiple datasets. Each input dataset is assumed to contain a 'queenframe'
(an averaged registered image) and a 'cleanqueen' (an image delineating individual
chromatophore territories) stored in its 'stitching' group.

For every consecutive dataset pair (dataset1 → dataset2, dataset2 → dataset3, …, datasetN–1 → datasetN),
the user is prompted to manually select corresponding points via the ImagePointSelector GUI.
These manual alignments are then used to compute a full matrix of initial affine transforms,
which is then supplied to the chunkstitching function to compute dense registration maps.

All datasets are warped into the coordinate system of the last (newest) dataset
(which is assumed to contain the most chromatophores, including new additions) and averaged
to produce a merged superframe (the combined queenframe) and superclean (the combined cleanqueen).

Additionally, pairwise chromatophore ID mappings are computed between consecutive datasets,
so that the identity of chromatophores can be tracked over time.

The final results—including the superframe, superclean, registration maps, and ID mappings—
are saved into the reference dataset’s Zarr store (under group 'superstitch'), and a complete meta‑dataset
(an xarray.Dataset) is saved under group 'supermeta'.
"""

import cv2
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import itertools

# Updated import paths using "..stitching" and "..utils"
from ..stitching.stitching import (
    draw_centers_on_masterframes,
    chunkstitching
)
from ..stitching.image_point_selector import ImagePointSelector
from ..utils.utils import clear_edges, cuttlefish_mask


###########################################################################
# Helper: Convert image for selector (ensure 8-bit BGR)
###########################################################################
def convert_for_selector(image: np.ndarray) -> np.ndarray:
    """
    Convert an image to 8-bit BGR format.
    If the image is not uint8, normalize to 0-255.
    If the image is grayscale, convert to BGR.
    """
    if image.dtype != np.uint8:
        imin, imax = np.min(image), np.max(image)
        if imax > imin:
            image_norm = ((image - imin) / (imax - imin) * 255).astype(np.uint8)
        else:
            image_norm = np.zeros_like(image, dtype=np.uint8)
    else:
        image_norm = image.copy()
    if image_norm.ndim == 2:
        image_norm = cv2.cvtColor(image_norm, cv2.COLOR_GRAY2BGR)
    return image_norm

###########################################################################
# Local: Match chromatophore IDs between cleanqueen images
###########################################################################
def match_chromatophore_ids(cleanqueen1: np.ndarray, cleanqueen2: np.ndarray, reg_map: np.ndarray) -> dict:
    """
    Match chromatophore IDs from cleanqueen1 to cleanqueen2 using the registration map.
    Each cleanqueen is a 2D array of integer labels (0 = background).
    Returns a dictionary mapping each label in cleanqueen1 to the best matching label in cleanqueen2.
    """
    mapping = {}
    labels1 = np.unique(cleanqueen1)
    labels1 = labels1[labels1 != 0]  # ignore background
    for label in labels1:
        mask1 = (cleanqueen1 == label)
        warped_mask = cv2.remap(mask1.astype('float32'), reg_map, None, interpolation=cv2.INTER_NEAREST)
        warped_mask = warped_mask > 0.5
        labels2 = np.unique(cleanqueen2)
        labels2 = labels2[labels2 != 0]
        best_overlap = 0.0
        best_label = None
        for l2 in labels2:
            mask2 = (cleanqueen2 == l2)
            intersection = np.logical_and(warped_mask, mask2).sum()
            union = np.logical_or(warped_mask, mask2).sum()
            if union > 0:
                overlap = intersection / union
                if overlap > best_overlap and overlap > 0.1:
                    best_overlap = overlap
                    best_label = l2
        mapping[label] = best_label
    return mapping

###########################################################################
# Main Superstitching Function
###########################################################################
def superstitching(dataset_paths: list,
                    grid_size: int,
                    patch_size: int,
                    coarse_grid_size: int,
                    initial_estimate: str,
                    search_space: str,
                    clear_edge: int,
                    center_threshold: float,
                    mask_inner: bool,
                    mask_dilation_iterations: int,
                    mls_alpha: float,
                    ransac_tolerance: float,
                    debug: bool,
                    debug_visual: bool) -> None:
    """
    Process multiple datasets to create a super-dataset.
    [Docstring omitted for brevity; see previous version]
    """
    print("Loading queenframes and cleanqueens from datasets...")
    queenframes = []
    cleanqueens = []
    for path in dataset_paths:
        ds = xr.open_zarr(path, group='stitching')
        qf = ds.queenframe.data.compute()
        try:
            cq = ds.cleanqueen.data.compute()
        except Exception:
            cq = (qf > 0.5).astype('uint8')
        queenframes.append(qf)
        cleanqueens.append(cq > 0)
    
    if len(queenframes) < 2:
        raise RuntimeError("At least two datasets are required for superstitching.")
    
    n = len(queenframes)
    ref = n - 1  # Use the last dataset as the reference.
    
    print("Computing center images from queenframes...")
    mfs_points = []
    masks = []
    for qf, cq in zip(queenframes, cleanqueens):
        mfp = draw_centers_on_masterframes(qf.copy(), cq.copy(), threshold=center_threshold)
        mfs_points.append(mfp)
        masks.append(cq)
    
    print("Performing manual alignment for all dataset pairs...")
    # Compute a full matrix of manual alignment transforms
    initial_affine_transforms = np.zeros((n, n, 2, 3), dtype='float32')
    for i, j in itertools.combinations(range(n), 2):
        print(f"Aligning dataset {i} → dataset {j} manually...")
        img1 = convert_for_selector(queenframes[i])
        img2 = convert_for_selector(queenframes[j])
        selector = ImagePointSelector(img1, img2)
        selector.get_point_pairs()  # Manual point selection
        transformation_matrix_i2j, transformation_matrix_j2i = selector.estimate_transformations()
        if debug:
            print(f"[DEBUG] Transformation from dataset {i} → {j}:\n{transformation_matrix_i2j}")
            print(f"[DEBUG] Transformation from dataset {j} → {i}:\n{transformation_matrix_j2i}")
        initial_affine_transforms[i, j] = transformation_matrix_i2j
        initial_affine_transforms[j, i] = transformation_matrix_j2i
    
    print("Computing registration maps (via chunkstitching) to align all datasets to the reference...")
    reg_matrices = chunkstitching(
        mfs=np.array(mfs_points),
        masks=np.array(masks),
        trg_chunk_idx=ref,
        patch_size=patch_size,
        grid_size=grid_size,
        coarse_grid_size=coarse_grid_size,
        initial_estimate=initial_estimate,
        mls_alpha=mls_alpha,
        ransac_tolerance=ransac_tolerance,
        search_space=tuple(tuple(None if x=='None' else float(x) for x in s.split(';'))
                           for s in search_space.split(',')),
        debug=debug,
        debug_visual=debug_visual,
        initial_affine_transforms=initial_affine_transforms
    )
    
    # Force the registration map for the reference dataset to be the identity.
    full_height, full_width = queenframes[0].shape
    H_coarse = (full_height + 2 * grid_size - 1) // grid_size
    W_coarse = (full_width + 2 * grid_size - 1) // grid_size
    identity_map = np.stack(np.meshgrid(np.arange(W_coarse), np.arange(H_coarse)), axis=-1).astype(np.float32)
    reg_matrices[ref] = identity_map  # Fixed: assign identity_map to reg_matrices[ref]


    if debug:
        print("Registration map statistics:")
        for i in range(n):
            reg = reg_matrices[ref, i]
            nan_count = np.isnan(reg).sum()
            print(f"[DEBUG] Mapping dataset {i} -> {ref}: min={np.nanmin(reg):.2f}, max={np.nanmax(reg):.2f}, mean={np.nanmean(reg):.2f}, NaNs={nan_count}")
            if debug_visual:
                plt.figure()
                plt.title(f"Registration map dataset {i} -> {ref}")
                plt.imshow(reg)
                plt.colorbar()
                plt.show()
    
    if np.isnan(reg_matrices).any():
        raise RuntimeError("Registration maps contain NaN values. Check manual alignment or adjust RANSAC tolerance.")
    
    grow_t = np.array([[grid_size, 0, 0],
                       [0, grid_size, 0]], dtype='float32')
    
    print("Warping queenframes and cleanqueens to reference coordinates...")
    aligned_qfs = []
    aligned_cqs = []
    for i in range(n):
        if i == ref:
            aligned_qfs.append(queenframes[i])
            aligned_cqs.append(cleanqueens[i].astype('float64'))
        else:
            reg_map = cv2.warpAffine(reg_matrices[i].astype(np.float32), grow_t, (full_width, full_height))
            warped_qf = cv2.remap(queenframes[i].astype('float64'),
                                reg_map, None,
                                interpolation=cv2.INTER_LINEAR)
            warped_cq = cv2.remap(cleanqueens[i].astype('float64'),
                                reg_map, None,
                                interpolation=cv2.INTER_NEAREST)
            aligned_qfs.append(warped_qf)
            aligned_cqs.append(warped_cq)

    
    superframe = np.mean(np.stack(aligned_qfs, axis=0), axis=0)
    superclean = np.mean(np.stack(aligned_cqs, axis=0), axis=0)
    
    print("Computing chromatophore ID mappings between consecutive datasets...")
    id_mappings = []
    for i in range(n - 1):
        pair_mfs = np.array([mfs_points[i], mfs_points[i+1]])
        pair_masks = np.array([masks[i], masks[i+1]])
        pair_reg = chunkstitching(
            mfs=pair_mfs,
            masks=pair_masks,
            trg_chunk_idx=1,
            patch_size=patch_size,
            grid_size=grid_size,
            coarse_grid_size=coarse_grid_size,
            initial_estimate=initial_estimate,
            mls_alpha=mls_alpha,
            ransac_tolerance=ransac_tolerance,
            search_space=tuple(tuple(None if x=='None' else float(x) for x in s.split(';'))
                               for s in search_space.split(',')),
            debug=debug,
            debug_visual=debug_visual,
            initial_affine_transforms=None
        )
        # FIX: Use pair_reg[0] (the mapping from dataset i into dataset i+1) instead of incorrect indexing.
        pair_reg_map = cv2.warpAffine(pair_reg[0].astype(np.float32), grow_t, (full_width, full_height))
        mapping = match_chromatophore_ids(cleanqueens[i], cleanqueens[i+1], pair_reg_map)
        if debug:
            print(f"[DEBUG] Chromatophore ID mapping from dataset {i} to {i+1}: {mapping}")
        id_mappings.append(mapping)
    
    print("Saving super-dataset results...")
    output_path = dataset_paths[-1]
    xr.DataArray(superframe, dims=['x', 'y'], name='superframe')\
      .to_zarr(output_path, group='superstitch', mode='a')
    xr.DataArray(superclean, dims=['x', 'y'], name='superclean')\
      .to_zarr(output_path, group='superstitch', mode='a')
    
    # FIX: Correct the dimension names for the registration matrices.
    meta_ds = xr.Dataset({
        'queenframes': (['dataset', 'x', 'y'], np.stack(queenframes, axis=0)),
        'cleanqueens': (['dataset', 'x', 'y'], np.stack(cleanqueens, axis=0).astype(np.int32)),
        'registration_matrices': (['src_dataset', 'grid_x', 'grid_y', 'coord'], reg_matrices),
        'aligned_queenframes': (['dataset', 'x', 'y'], np.stack(aligned_qfs, axis=0)),
        'aligned_cleanqueens': (['dataset', 'x', 'y'], np.stack(aligned_cqs, axis=0)),
        'superframe': (['x', 'y'], superframe),
        'superclean': (['x', 'y'], superclean)
    }, attrs={
        'n_datasets': n,
        'description': 'Meta-dataset from superstitching: includes raw and aligned queenframes, cleanqueens, registration maps, and merged superframe/superclean.'
    })

    
    meta_ds.to_zarr(output_path, group='supermeta', mode='a')
    print(f"Superstitching complete. Superframe and superclean saved to {output_path} under 'superstitch', and meta-dataset saved under 'supermeta'.")
