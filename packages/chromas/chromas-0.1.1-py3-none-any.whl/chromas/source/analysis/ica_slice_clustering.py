import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
from skimage.segmentation import mark_boundaries
from matplotlib.patches import Wedge
import matplotlib.collections as collections
import decord
import click
import matplotlib
import zarr
from ..utils.decorators import error_handler
from ..utils.decorators import convergence_handler
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from .clustering_utils import cluster_correlation


def plot_ICs_per_chrom(dataset, chunk_int, ica, name, output_dir):
	max_n_ICs = ica.elbow_point.max().data.compute()

	plt.figure(figsize=(4, 2))

	plt.hist(ica.elbow_point.data.compute(), bins=np.arange(1, max_n_ICs+2)-0.5, rwidth=0.8)[0]
	plt.xticks(np.arange(1, max_n_ICs+1))

	plt.xlabel('# ICs')
	plt.ylabel('# chromatophores')
	plt.title('# ICs per chromatophore')

	# Remove top right  and top spines
	plt.gca().spines['top'].set_visible(False)
	plt.gca().spines['right'].set_visible(False)


	plt.savefig(f'{output_dir}/n_ics_per_chromatophore_{name}_chunk{chunk_int}.png', dpi=600, bbox_inches='tight')
	click.secho(f'{ica.elbow_point.mean().data.compute():.2f} +/- {ica.elbow_point.std().data.compute():.2f} (mean +/- std) ICs per chrom. (n={ica.sizes["chrom_id"]})')


def plot_radial_influence(percentage_influence, C, dir_radial, name, chunk_int, rotation_slices=0):

	num_slices = percentage_influence.shape[0]
	angles = np.linspace(0, 2 * np.pi, num_slices, endpoint=False).tolist()

	# Add the first angle to close the circle
	angles += angles[:1]

	# Convert slice-based rotation to radians
	rotation_radians = (2 * np.pi / num_slices) * rotation_slices
	
	# Apply rotation to all angles
	angles = [(angle + rotation_radians) % (2 * np.pi) for angle in angles]

	# Create the first plot with everything
	plt.figure(figsize=(6, 6), dpi=600)
	ax = plt.subplot(111, polar=True)

	# Plot influence of each IC on slices with labels, grid, and everything
	for i in range(percentage_influence.shape[1]):  # Loop through each IC
		values = percentage_influence[:, i].tolist()
		values += values[:1]  # Ensure the loop is closed
		line, = ax.plot(angles, values, linewidth=2, linestyle='solid', label=f'IC {i+1}')
		ax.fill(angles, values, alpha=0.1, color=line.get_color())  # Fill under the curve with IC color

		# Find the peak influence (maximum value) for the IC
		peak_index = np.argmax(percentage_influence[:, i])  # Index of peak value
		peak_angle = angles[peak_index]  # Angle corresponding to the peak

		# Draw a line at the peak of the influence with the same color as the IC
		ax.plot([peak_angle, peak_angle], [0, 100], linestyle='dashed', linewidth=2, color=line.get_color())

	# Highlight the first slice with a black line
	ax.plot([angles[0], angles[0]], [0, 100], color='black', linewidth=3, linestyle='--', label='First Slice')

	# Set labels and title
	ax.set_title(f"Independent components' influence on slices (chrom {C})", size=16, pad=20)
	ax.set_theta_offset(np.pi / 2)
	ax.set_theta_direction(-1)
	
	# Set slice labels around the circle
	ax.set_xticks(angles[:-1])
	ax.set_xticklabels([f'slice {i+1}' for i in range(num_slices)], size=10)

	# Set radial limits and grid
	ax.set_ylim(0, 100)  # Influence in percentage, so limit from 0 to 100

	# Show legend
	plt.legend(loc='upper right', bbox_to_motion_marker=(1.1, 1.1))
	plt.tight_layout()

	plt.savefig(f'{dir_radial}/influence_radial_{name}_chunk{chunk_int}_chrom_{C}.png', dpi=600, bbox_inches='tight')
	plt.close()
			

@error_handler('ICA slice clustering')
def ica_slice_cluster(dataset: str, chunk_int: int, method: str = 'AffinityPropagation', clustering_kwargs: dict = {}, max_tries: int = 5,
					  nr_slices: int = 36,
					  debug_args: dict = {'debug': False, 'debug_visual': False}):
	# LOAD DATA:
	if isinstance(chunk_int, int):
		ica_group = f'ica_chunk_{chunk_int}'
		click.echo(f'Using chunk {chunk_int} for ICA.')
	else:
		ica_group = 'ica'
		chunk_int = xr.open_zarr(dataset, group='stitching').stitching_matrix.attrs['ref_chunk']
		click.echo(f'Using chunk {chunk_int} as reference chunk for ICA.')
	ica = xr.open_zarr(dataset, group=ica_group)
	chroms2analyse = ica.chrom_id.data
	max_n_ICs = ica.elbow_point.max().data.compute()
	if debug_args['debug']:
		click.echo(f'{len(chroms2analyse)} chromatophores with up to {max_n_ICs} ICs per chromatophore.')

	# LOAD ICs:    
	ICs = np.zeros((len(chroms2analyse), max_n_ICs, ica.ica_sources.sizes['diff']))
	IC_mask = np.zeros((len(chroms2analyse), max_n_ICs), dtype=bool)
	IC_mask.fill(False)
	chroms2remove = []
	chroms2remove_mask = np.ones((len(chroms2analyse)), dtype=bool)
	for i, c in tqdm(enumerate(chroms2analyse), desc='Load IC sources for all chroms', unit='chrom'):
		n_ic = int(ica.elbow_point.sel(chrom_id=c).data.compute())
		ICs[i, :n_ic] = ica.ica_sources.sel(chrom_id=c).data.compute()[:, :n_ic].T
		IC_mask[i, :n_ic] = True

		if n_ic == 0:
			chroms2remove.append(c)
			chroms2remove_mask[i] = False

	chroms2analyse = [c for c in chroms2analyse if c not in chroms2remove]
	click.echo(f'Excluded {len(chroms2remove)} chromatophores from analysis due to errors in individual ICA for that chromatophores.')

	ICs = ICs[chroms2remove_mask]
	IC_mask = IC_mask[chroms2remove_mask]

	# np.savez('tmp.npz', ICs=ICs, IC_mask=IC_mask, chroms2analyse=np.array(chroms2analyse))
	# ICs, IC_mask, chroms2analyse = np.load('tmp.npz')['ICs'], np.load('tmp.npz')['IC_mask'], np.load('tmp.npz')['chroms2analyse']
	ICs = xr.DataArray(ICs, dims=('chrom_id', 'IC', 'time'), coords={'chrom_id': chroms2analyse, 'IC': np.arange(max_n_ICs), 'time': np.arange(ica.ica_sources.sizes['diff'])})
	IC_mask = xr.DataArray(IC_mask, dims=('chrom_id', 'IC'), coords={'chrom_id': chroms2analyse, 'IC': np.arange(max_n_ICs)})

	if debug_args['debug']:
		click.echo(f'{IC_mask.sum().data} ICs in total.')

	click.secho(f'Compute correlation matrix for {IC_mask.sum().data} IC sources ({ICs.data[IC_mask.data].shape=}).')
	corr = np.abs(np.corrcoef(ICs.data[IC_mask.data]))
	if debug_args['debug']:
		click.echo(f'{corr.shape=}')
	if debug_args['debug_visual']:
		plt.imshow(corr, cmap='Blues')
		plt.title("Correlation matrix")
		plt.xlabel("IC")
		plt.ylabel("IC")
		plt.colorbar()
		plt.show()
	labels_ = convergence_handler(cluster_correlation, max_tries=max_tries)(corr, method, **clustering_kwargs)

	# np.save('.tmp_labels', labels_)

	# labels_ = np.load('.tmp_labels.np.npy')

	dom_ics = ica.influence.argmax(dim='component').compute()
	if debug_args['debug']:
		click.echo(f'{len(chroms2analyse)=}\n{dom_ics=}\n{labels_.shape=}, {labels_.mean()=}, {labels_.min()=}, {labels_.max()=}')
	if debug_args['debug_visual']:
		plt.hist(dom_ics.data.flatten())
		plt.show()

	pi = ica.influence.compute()

	IC_labels = np.zeros((len(chroms2analyse), max_n_ICs), dtype=int) - 2
	IC_labels[IC_mask.data] = labels_
	IC_labels = xr.DataArray(IC_labels, dims=('chrom_id', 'IC'), coords={'chrom_id': chroms2analyse, 'IC': np.arange(max_n_ICs)})
	slice_labels = np.zeros((len(chroms2analyse), nr_slices), dtype=int)
	for c, chrom in enumerate(chroms2analyse):
		if np.isnan(pi.sel(chrom_id=chrom).data).any():
			click.secho(f'NaN found in influence vector of {chrom=}.')
			slice_labels[c] = -1
			continue
		for sl in range(nr_slices):
			try:
				slice_labels[c, sl] = IC_labels.sel(chrom_id=chrom, IC=dom_ics.sel(chrom_id=chrom, slice=sl)).data
			except IndexError:
				click.secho(f'Index Error: {c=}, {chrom=}, {sl=}', fg='red', bold=True, err=True)
				slice_labels[c, sl] = -1
			if slice_labels[c, sl] == -2:
				click.echo(f'\nchrom={chrom}, slice={sl}, dom_ic={dom_ics.sel(chrom_id=chrom, slice=sl).data}, elbow={int(ica.elbow_point.sel(chrom_id=chrom).data.compute())}')
				click.echo(f'\tIC_mask={IC_mask.sel(chrom_id=chrom, IC=dom_ics.sel(chrom_id=chrom, slice=sl)).data}, IC_label={IC_labels.sel(chrom_id=chrom, IC=dom_ics.sel(chrom_id=chrom, slice=sl)).data}, pi={pi.sel(chrom_id=chrom, slice=sl).data}')
	assert np.min(slice_labels) > -2
	slice_labels = xr.DataArray(slice_labels, dims=('chrom_id', 'slice'), coords={'chrom_id': chroms2analyse, 'slice': np.arange(nr_slices)})
	# chroms2analyse = xr.DataArray(chroms2analyse, dims=('chroms2analyse'), coords={'chroms2analyse', chroms2analyse})
	click.echo(f'Found {len(np.unique(labels_))} IC clusters.')

	chrom_ids = np.stack([chroms2analyse,]*nr_slices, axis=1)
	clustersize = np.array([len(np.unique(chrom_ids[slice_labels.data == label])) for label in range(slice_labels.data.max()+1)])

	# STORE DATA:
	zarr_store = zarr.open(dataset, mode='a')
	for var in ['IC_labels', 'slice_labels', 'clustersize', 'chroms2analyse']:
		if var in zarr_store[ica_group]:
			click.secho(f'WARNING: Removing {var} from dataset since it already exists.', italic=True)
			del zarr_store[f'{ica_group}/{var}']
			# Wait for the deletion to finish
			while var in zarr_store:
				pass
	ica = ica.assign({'IC_labels': IC_labels, 'slice_labels': slice_labels, 'clustersize': clustersize, 'chroms2analyse': chroms2analyse})
	ica.to_zarr(dataset, group=ica_group, mode='a')


@error_handler('Plotting slice cluster')
def plot_slice_cluster(dataset, chunk_int, cluster_sizes, output_dir, radial: bool=True, generate: bool = False,
					   show_cleanqueen: bool = False, show_skeleton: bool = False, show_lines: bool = False, show_mm: bool = False,
					   show_slices: bool = False, show_ics: bool = False, show_clustersize: bool = False):
	# LOAD DATA:
	if isinstance(chunk_int, int):
		ica_group = f'ica_chunk_{chunk_int}'
		click.echo(f'Using chunk {chunk_int} for plotting.')
	else:
		ica_group = 'ica'
		chunk_int = xr.open_zarr(dataset, group='stitching').stitching_matrix.attrs['ref_chunk']
		click.echo(f'Using chunk {chunk_int} as reference chunk for plotting.')
	ica = xr.open_zarr(dataset, group=ica_group)
	clustersize = ica.clustersize.data
	chroms2analyse = ica.chroms2analyse.data
	slice_labels = ica.slice_labels.sel(chrom_id=chroms2analyse).compute()
	
	chunk = xr.open_zarr(dataset, f'chunk_{chunk_int}')
	try:
		image = chunk.chunkaverage.data.compute()
	except Exception as e:
		click.secho(f'[WARNING] {e}\nTake first frame from first chunk video instead.', fg='yellow', bold=True)
		image = decord.VideoReader(chunk.segmentation.attrs['chunk_path']).next().asnumpy()
	cleanqueen = chunk.cleanqueen.compute()
	mm = chunk.motion_marker_centers.sel(frame=0).compute()
	centers = chunk.centers.sel(frame=0, non_motion_marker=chroms2analyse).compute()
	orientation_angles = chunk.orientation_angles.sel(frame=0, non_motion_marker=chroms2analyse).compute()
	slice_areas = chunk.slice_areas.sel(frame=0, non_motion_marker=chroms2analyse).compute()
	nr_slices = nr_slices


	# PREPARE OUTPUT DIRECTORY:
	name = dataset.split('/')[-1].split('.')[0]
	if output_dir is None:
		output_dir = os.path.dirname(dataset)
	dir_ICS = f'{output_dir}/ICs'

	if radial:
		dir_radial = f'{output_dir}/radial IC influence plots'
		os.makedirs(dir_radial, exist_ok=True)
	os.makedirs(output_dir, exist_ok=True)
	os.makedirs(dir_ICS, exist_ok=True)


	# PLOT ICs PER CHROMATOPHORE:
	if show_ics:
		plot_ICs_per_chrom(dataset, chunk_int, ica, name, output_dir)
		if radial:
			for C in np.random.choice(ica.chrom_id.data, 30):
				plot_radial_influence(ica.influence.sel(chrom_id=C).data.compute()[:, :ica.elbow_point.sel(chrom_id=C).data.compute()], C, dir_radial, name, chunk_int)


	# PLOT CLUSTERSIZE HISTOGRAM:
	if show_clustersize:
		click.secho('Plotting `#chroms per cluster` histograms')
		plt.figure()
		plt.hist(clustersize, bins=np.arange(1, clustersize.max()+2)-0.5, rwidth=0.8)
		plt.xlabel('clustersize')
		plt.ylabel('# clusters')
		plt.gca().spines['top'].set_visible(False)
		plt.gca().spines['right'].set_visible(False)
		if generate:
			plt.savefig(f'{output_dir}/clustersize_{name}_chunk{chunk_int}.png', dpi=600, bbox_inches='tight')
		else:
			plt.gcf().canvas.manager.set_window_title('CHROMAS - Plot Clustersize')
			plt.show()
		plt.close()
		
	click.secho(f'{np.mean(clustersize):.2f} +/- {np.std(clustersize):.2f} (mean +/- std) chroms per cluster. (n={len(clustersize)})\nChroms per cluster:')
	for p in [5, 10, 25, 50, 75, 90, 95]:
		click.secho(f'\t{p}%:\t{np.percentile(clustersize, p):.2f}')


	# PLOT SLICEQUEEN
	click.secho('Plotting slicequeen')
	plt.figure(figsize=(10, 10))
	if show_cleanqueen:
		plot_frame = mark_boundaries(image, cleanqueen, color=(1, 1, 1), outline_color=None)
	else:
		plot_frame = image
	plt.imshow(plot_frame)

	if cluster_sizes:
		chrom_ids = np.stack([chroms2analyse,]*nr_slices, axis=1)
		K = int(slice_labels.data.max() + 1)
		clustersize = np.array([len(np.unique(chrom_ids[slice_labels.data == label])) for label in range(K)])
		labels2plot = [label for label, n_chrom in zip(range(K), clustersize) if n_chrom in cluster_sizes]
		chroms2analyse = np.unique(slice_labels.where(slice_labels.isin(labels2plot), drop=True).chrom_id.data) 
	else:
		labels2plot = slice_labels.data.flatten()
		labels2plot = labels2plot[labels2plot >= 0]
	labels2plot = np.unique(labels2plot)

	if show_slices:
		# This is tricky: angles in the previous steps are computed as angles counterclockwise from the y-axis. But in matplotlib (Wedges), they have to be given
		# as angles clockwise from the x-axis. So we have to subtract the angles from nr_slices0 to correct for counterclockwise/clockwise difference, and then subtract 90
		# for the x-axis/y-axis difference. Hence angle_matplotlib = nr_slices0 - angle_computed - 90 = 270 - angle_computed. Furthermore, we have t iterate over the areas 
		# in reversed order, because matplotlib expects the angles in clockwise order.
		wedges = [
			Wedge(
				(centers.sel(non_motion_marker=chrom)[1], centers.sel(non_motion_marker=chrom)[0]),
					slice_area,
					270 - orientation_angles.sel(non_motion_marker=chrom) + angle,
					270 - orientation_angles.sel(non_motion_marker=chrom) + angle + nr_slices0//nr_slices,
					alpha=float(label in labels2plot),
					color=matplotlib.colormaps['gist_rainbow'](np.where(labels2plot==label)[0][0]/len(labels2plot)) if label in labels2plot else 'white'
				) for chrom in chroms2analyse for angle, slice_area, label in
							zip(reversed(np.linspace(0, nr_slices0, nr_slices+1)[:-1]), slice_areas.sel(non_motion_marker=chrom).data, slice_labels.sel(chrom_id=chrom).data)
		]

		plt.gca().add_collection(collections.PatchCollection(wedges, match_original=True))

	if show_skeleton:
		tri = Delaunay(mm)
		plt.triplot(mm[:, 1], mm[:, 0], tri.simplices, color='white' if not show_cleanqueen else 'dodgeblue', alpha=.5, lw=0.5)
	
	if show_mm:
		plt.plot(mm[:, 1], mm[:, 0], 'o', color='white' if not show_cleanqueen else 'dodgeblue', markersize=1, alpha=.5)

	if show_lines:
		for i, label in enumerate(labels2plot):
			cluster_chroms = slice_labels.where(slice_labels == label, drop=True).chrom_id.data
			assert len(cluster_chroms) in cluster_sizes
			cens = np.array([centers.sel(non_motion_marker=chrom).data for chrom in cluster_chroms])
			if len(cens) < 3:
				plt.plot(cens[:, 1], cens[:, 0], color=matplotlib.colormaps['gist_ncar']((i%10)/10))
				continue
			ch = ConvexHull(cens)
			for simplex in ch.simplices:
				plt.plot(cens[simplex, 1], cens[simplex, 0], color=matplotlib.colormaps['gist_ncar']((i%10)/10))

	plt.axis('off')

	if cluster_sizes:
		plt.title('Slicequeen with clusters of size: ' + ', '.join(map(str, cluster_sizes)))
	else:
		plt.title('Slicequeen')
	if generate:
		plt.savefig(f'{output_dir}/slicequeen_{name}_chunk_{chunk_int}.png', dpi=600, bbox_inches='tight')
	else:
		plt.gcf().canvas.manager.set_window_title('CHROMAS - Plot Slicequeen')
		plt.show()
	plt.close()