import click
import os
import subprocess
import re
import functools
from trogon import tui
from .source.utils.decorators import debug_handler, timing_handler

timeit = False
LOG_FILE = "runs.log"
STATUS_FILE = "runs.status"

@tui()
@click.group()
def cli():
	pass

@cli.command()
def version():
	"""Prints version."""
	click.echo("Chromas version 1.0.0")

#########################################################################################################################################################!
############################ UTILITY FUNCTIONS ##########################################################################################################!
#########################################################################################################################################################!
def parse_integers(ctx, param, value) -> list[int]:
	""" Parse string comma seperated integers as list of integers. """
	if not value:  # If no input is provided, return an empty list
		return []
	try:
		return [int(x) for x in value.split(',')]
	except ValueError:
		raise click.BadParameter('List must contain integers.')


def merge_task_options(tasks) -> list[click.Option]:
	""" Merge all options from tasks into the run command. """
	params = []
	for task in tasks:
		for param in task.params:
			if param not in params:  # Avoid duplicate options
				if isinstance(param, click.Argument):
					# Convert required arguments to optional except for video_file
					if param.name != 'video_file':
						param = click.Option(
							[f"--{param.name}"], type=param.type, help=f"Optional: {param.name}", hidden=(param.name == "dataset")
						)
				params.append(param)
	return params


def ensure_directory_exists(path):
	os.makedirs(path, exist_ok=True)
	

def update_status_file(video_id, status, status_file):
	# Ensure the status file exists
	if not os.path.exists(status_file):
		with open(status_file, "w") as status_f:
			pass  # Create an empty file if it doesn't exist

	with open(status_file, "r+") as status_f:
		lines = status_f.readlines()
		status_f.seek(0)
		found = False
		for line in lines:
			if line.startswith(video_id):
				status_f.write(f"{video_id}: {status}\n")
				found = True
			else:
				status_f.write(line)
		if not found:
			status_f.write(f"{video_id}: {status}\n")
		status_f.truncate()


#########################################################################################################################################################!
####################################  TASKS  ############################################################################################################!
#########################################################################################################################################################!
@cli.command()
@click.argument('video_file', type=click.Path(exists=True))
@click.option('-o', '--output-name', type=click.Path(), help='Path or name to save dataset.')
@click.option('-od', '--output-dir', type=click.Path(), help='Directory to save chunked video files.')
@click.option('-f', '--force-overwrite', is_flag=True, show_default=True, default=False, help='Overwrite existing output file.')
@click.option('-fs', '--focus-statistic', type=click.Choice(['dog']), default='dog', show_default=True, help='Statistic to use for focus detection.')
@click.option('-ft', '--focus-threshold', type=float, default=0.01, show_default=True, help='Threshold for focus detection.')
@click.option('-on', '--onset', type=int, default=0, show_default=True, help='Number of frames to remove from the beginning and end of each chunk.')
@click.option('-md', '--min-chunk-duration', type=int, default=100, show_default=True, help='Minimum duration of a chunk in frames.')
@click.option('--sigma1', 'sigma_1', type=float, default=2.0, show_default=True, help='Sigma for first Gaussian filter.')
@click.option('--sigma2', 'sigma_2', type=float, default=1.0, show_default=True, help='Sigma for second Gaussian filter.')
@click.option('--size1', 'size_1', type=int, default=11, show_default=True, help='Size of first Gaussian filter.')
@click.option('--size2', 'size_2', type=int, default=5, show_default=True, help='Size of second Gaussian filter.')
@click.option('--dog-threshold', 'threshold', type=float, default=4.0, show_default=True, help='Threshold for DoG.')
@click.option('--processes', is_flag=True, show_default=True, default=True, help='Use processes instead of threads.')
@click.option('-n', '--n-workers', type=int, default=4, show_default=True, help='Number of workers to use.')
@click.option('-t', '--threads-per-worker', type=int, default=4, show_default=True, help='Number of threads per worker.')
def chunk(video_file, output_name, output_dir, force_overwrite, focus_statistic, focus_threshold, onset, min_chunk_duration,
		  sigma_1, sigma_2, size_1, size_2, threshold, processes, n_workers, threads_per_worker) -> None:
	""" Chunk video into usable segments. """
	from .source.chunking.chunking import chunking

	cluster_args = {'processes': processes, 'n_workers': n_workers, 'threads_per_worker': threads_per_worker}
	
	focus_parameters = {
		'sigma_1': sigma_1,
		'sigma_2': sigma_2,
		'size_1': size_1,
		'size_2': size_2,
		'threshold': threshold
	}

	if timeit:
		chunking = timing_handler(timeit)(chunking)

	succ, file = chunking(video_file, focus_statistic, focus_parameters, focus_threshold, onset, min_chunk_duration, output_dir, output_name,
			 force_overwrite, cluster_args)
	return file


@cli.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.option('-e', '--nr-epochs', type=int, default=100, show_default=True, help='Number of epochs to train for.')
@click.option('-v', '--val-every-n-epochs', type=int, default=5, show_default=True, help='Validate every n epochs.')
@click.option('-m', '--method', type=click.Choice(['randomforest', 'rf', 'lookup', 'lookup_table', 'fcn_resnet50',
	'fcn_resnet101', 'deeplabv3_resnet101', 'deeplabv3_resnet50', 'deeplabv3_mobilenet_v3_large', 'unet']),
	default='fcn_resnet50', help='Method for segmentation.')
@click.option('-p', '--pretrained', type=bool, default=True, help='Path to weights of pretrained model.')
@click.option('-c', '--nr-classes', type=int, default=4, show_default=True, help='Number of classes to predict.')
@click.option('-o', '--output-dir', type=click.Path(), default=None, help='Directory to save model weights and plots.')
@click.option('-w', '--weights', type=click.Path(), default=None, help='Path to weights of pretrained model.')
def train(input_dir, nr_epochs, val_every_n_epochs, method, pretrained, nr_classes, output_dir, weights) -> None:
	""" Train neural network classifier. """
	match method:
		case 'unet':
			from .source.training.unet_training import train
			train(input_dir, nr_epochs, val_every_n_epochs, method, pretrained, nr_classes, output_dir, weights)
		case 'randomforest' | 'rf':
			from .source.training.random_forest_training import train
			train(input_dir, output_dir)
		case 'lookup' | 'lookup_table':
			raise NotImplementedError('Lookup tables are to be trained at the beginning of the respective segmentation task (i.e. `chromas segment -m lookup`). This might change in a future release.')
		case _:
			from .source.training.neural_net_training import train
			train(input_dir, nr_epochs, val_every_n_epochs, method, pretrained, nr_classes, output_dir, weights)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-m', '--method', type=click.Choice(['neuralnet', 'nn', 'unet', 'randomforest', 'rf', 'lookup']), default='neuralnet', help='Method for segmentation.')
# General options
@click.option('-w', '--weights', type=click.Path(exists=False), show_default=False, default='default', help='Path to trained model.')
@click.option('--n-classes', type=int, default=2, show_default=True, help='Number of classes to predict.')
@click.option('-n', '--n-workers', type=int, default=1, show_default=True, help='Number of workers to use.')
@click.option('-t', '--threads-per-worker', type=int, default=1, show_default=True, help='Number of threads per worker.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
# Neural net options
@click.option('-a', '--architecture', type=click.Choice(['fcn_resnet50']), default='fcn_resnet50', show_default=True, help='Model architecture to use for neural net based segmentation.')
@click.option('-gpu', '--gpu', is_flag=True, show_default=True, default=False, help='Run neural net segmentation on GPU.')
# Lookup options
@click.option('--n-points-per-cluster', type=int, default=1, show_default=True)
@debug_handler()
def segment(dataset, method, weights, n_classes, n_workers, threads_per_worker, debug, debug_visual,
			architecture, gpu, n_points_per_cluster) -> None:
	""" Segment chromatophores."""
	cluster_args = {'n_workers': n_workers, 'threads_per_worker': threads_per_worker}
	debug_args = {'debug': debug, 'debug_visual': debug_visual}

	match method:
		case 'lookup':
			if weights == 'default':
				weights = None
			from .source.segmentation.segmentation_lookup import segmentation
			segmentation = functools.partial(segmentation, n_points_per_cluster=n_points_per_cluster)

		case 'randomforest':
			from .source.segmentation.segmentation_randomforest import segmentation
		
		case 'neuralnet':
			n_workers = threads_per_worker = 1
			if weights == 'default':
				weights = 'chromas\data\model_weights\fcn_resnet50_100_best_model.pth'  #TODO: Fix if not working.
			if gpu:
				click.echo('Loading videos for segmentation on GPU: enabled.')
				from .source.segmentation.segmentation_neuralnet_gpu import segmentation
			else:
				click.echo('Loading videos for segmentation on GPU: disabled.')
				from .source.segmentation.segmentation_neuralnet import segmentation
			segmentation = functools.partial(segmentation, architecture=architecture)

	if timeit:
		segmentation = timing_handler(timeit)(segmentation)
	
	segmentation(dataset, weights=weights, n_classes=n_classes, cluster_args=cluster_args, debug_args=debug_args)



@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-m', '--max-num-points-to-detect', type=int, default=900, show_default=True, help='Maximum number of points to detect.')
@click.option('-tgs', '--track-grid-size', type=int, default=100, show_default=True, help='Size of grid for point detection.')
@click.option('-igs', '--interpolate-grid-size', type=int, default=16, show_default=True, help='Size of grid for point interpolation.')
@click.option('--window-size', type=int, default=21, show_default=True, help='Size of window for point detection.')
@click.option('--max-distance', type=int, default=10, show_default=True, help='Maximum distance between points to consider them the same.')
@click.option('--mls-alpha', type=float, default=3.0, show_default=True, help='Alpha parameter for moving least squares.')
@click.option('--min-num-points-to-detect', type=int, default=40, show_default=True, help='Minimum number of points to detect.')
@click.option('--min-area', type=int, default=10, show_default=True, help='Minimum area of chromatophore to consider.')
@click.option('--max-area', type=int, default=1_000, show_default=True, help='Maximum area of chromatophore to consider.')
@click.option('--eccentricity', type=float, default=0.7, show_default=True, help='Threshold for eccentricity of chromatophore.')
@click.option('--solidity', type=float, default=0.7, show_default=True, help='Threshold for solidity of chromatophore.')
@click.option('--compute-videos', type=bool, show_default=True, default=True, help='Compute videos of chromatophore activity.')
@click.option('--masterframe-only', is_flag=True, show_default=True, default=False, help='Only compute masterframe.')
@click.option('--processes', is_flag=True, show_default=True, default=True, help='Use processes instead of threads.')
@click.option('-n', '--n-workers', type=int, default=4, show_default=True, help='Number of workers to use.')
@click.option('-t', '--threads-per-worker', type=int, default=4, show_default=True, help='Number of threads per worker.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
@debug_handler()
def register(dataset, max_num_points_to_detect,  track_grid_size, interpolate_grid_size, max_distance, mls_alpha, window_size,
			 min_num_points_to_detect, min_area, max_area, eccentricity, solidity, compute_videos, masterframe_only,
			 processes, n_workers, threads_per_worker, debug, debug_visual,) -> None:
	""" Register dataset to account for animal movement. """
	from .source.registration.registration import registration

	if timeit:
		registration = timing_handler(timeit)(registration)

	registration(dataset, min_num_points_to_detect, max_num_points_to_detect, 
			 	 window_size, track_grid_size, interpolate_grid_size,
				 max_distance, mls_alpha,
				 compute_videos, masterframe_only,
				 detection_args={'min_area': min_area, 'max_area': max_area, 'eccentricity': eccentricity, 'solidity': solidity},
				 cluster_args={'processes': processes, 'n_workers': n_workers, 'threads_per_worker': threads_per_worker},
				 debug_args={'debug': debug, 'debug_visual': debug_visual})


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-gs', '--grid-size', type=int, default=32, show_default=True, help='Size of grid of stitching map.')
@click.option('-ps', '--patch-size', type=int, default=64, show_default=True, help='Size of patches for stitching.')
@click.option('-cgs', '--coarse-grid-size', type=int, default=128, show_default=True, help='Size of grid for coarse point detection.')
@click.option('-ie', '--initial-estimate', type=str, default='rotation', show_default=True, help='Initial estimate for stitching.')
@click.option('-ss', '--search-space', type=str, default='512;2,0.35;0.035,None;None,None;None', show_default=True, help='Search space for stitching.')
@click.option('-ce', '--clear-edge', type=int, default=40, show_default=True, help='Number of pixels to clear from edge of image.')
@click.option('-ct', '--center-threshold', type=float, default=0.5, show_default=True, help='Threshold for center of chromatophore.')
@click.option('-mi', '--mask-inner', is_flag=True, show_default=True, default=False, help='Only use inner chromatophores for mask..')
@click.option('-mdi', '--mask-dilation-iterations', type=int, default=5, show_default=True, help='Number of dilation iterations for masking.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
@click.option('--mls-alpha', type=float, default=6.0, show_default=True, help='Alpha parameter for moving least squares.')
@click.option('--ransac-tolerance', type=float, default=1.0, show_default=True, help='Tolerance for RANSAC.')
@click.option('--manual', is_flag=True, show_default=True, default=False, help='Do not use mask for stitching.')
@click.option('--tutorial', is_flag=True, show_default=True, default=False, help='Use tutorial mode for stitching.')
@debug_handler()
def stitch(dataset, grid_size, patch_size, coarse_grid_size, initial_estimate, search_space, clear_edge, center_threshold,
		   mask_inner, mask_dilation_iterations, mls_alpha, ransac_tolerance, debug, debug_visual, manual, tutorial) -> None:
	""" Stitch chunks together. """
	from .source.stitching.stitching import stitching

	if timeit:
		stitching = timing_handler(timeit)(stitching)

	debug_args = {'debug': debug, 'debug_visual': debug_visual}

	if tutorial and not manual:
		click.secho("Do not forget to set the `--manual` flag.", fg='yellow')
		manual = True

	stitching(dataset, grid_size, patch_size, coarse_grid_size, initial_estimate, search_space, clear_edge, center_threshold,
			  mask_inner, mask_dilation_iterations, mls_alpha, ransac_tolerance, manual, tutorial, debug_args)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('--chunk-selection', callback=parse_integers, default='', help='Chunk to select.')
@click.option('-rb', '--remove-border', type=int, default=40, show_default=True, help='Number of pixels to remove from border of image.')
@click.option('-cqt', '--cleanqueen-threshold', type=float, default=0.01, show_default=True, help='Threshold for cleanqueen.')
@click.option('-ccq', '--compute-cleanqueen', type=bool, default=True, show_default=True, help='Wether to compute the cleanqueen.')
@click.option('-cqd', '--cleanqueen-dilation-iterations', type=int, default=10, show_default=True, help='Number of dilation iterations for cleanqueen.')
@click.option('-cma', '--cleanqueen-min-area', type=int, default=200, show_default=True, help='Minimum area (px) of chromatophore territory to consider.')
@click.option('--processes', is_flag=True, show_default=True, default=False, help='Use processes instead of threads.')
@click.option('-n', '--n-workers', type=int, default=4, show_default=True, help='Number of workers to use.')
@click.option('-t', '--threads-per-worker', type=int, default=4, show_default=True, help='Number of threads per worker.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
@debug_handler()
def area(dataset, chunk_selection, remove_border, cleanqueen_threshold, compute_cleanqueen, cleanqueen_dilation_iterations, cleanqueen_min_area,
		 processes, n_workers, threads_per_worker, debug, debug_visual) -> None:
	""" Track chromatophore sizes (areas). """
	from .source.areas.areas import areas

	if timeit:
		areas = timing_handler(timeit)(areas)

	cleanqueen_kwargs = {'threshold': cleanqueen_threshold, 'dilation_iterations': cleanqueen_dilation_iterations,
						 'remove_border': remove_border, 'min_area': cleanqueen_min_area}
	cluster_args = {'processes': processes, 'n_workers': n_workers, 'threads_per_worker': threads_per_worker}
	debug_args = {'debug': debug, 'debug_visual': debug_visual}

	areas(dataset, chunk_selection, compute_cleanqueen, cleanqueen_kwargs, cluster_args, debug_args)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('--n-slices', type=int, default=36, show_default=True, help='Number of slices to divide chromatophores into.')
@click.option('-n', '--n-workers', type=int, default=4, show_default=True, help='Number of workers to use.')
@click.option('-t', '--threads-per-worker', type=int, default=4, show_default=True, help='Number of threads per worker.')
@click.option('--processes', is_flag=True, show_default=True, default=False, help='Use processes instead of threads.')
@click.option('--buffer', type=int, default=40, show_default=True, help='Buffer to remove from frame edge in cleanqueen.')
@click.option('--area-cutoff', type=int, default=10_000, show_default=True, help='Maximum area of chromatophore to consider.')
@click.option('--max-ecc', type=float, default=0.6, show_default=True, help='Threshold for eccentricity of chromatophore.')
@click.option('--max-area', type=int, default=500, show_default=True, help='Threshold of maximum area of chromatophore to qualify as motion marker.')
@click.option('--max-cv', type=float, default=0.25, show_default=True, help='Threshold for coefficient of variation of chromatophore activity to qualify as motion marker.')
@click.option('--zero-consecutive', type=int, default=10, show_default=True, help='Threshold for maximum number of consecutive frames a chromatophore can disappear to still qualify as motion marker.')
@click.option('--zero-proportion', type=float, default=0.5, show_default=True, help='Threshold for maximum percentage of all frames a chromatophore can disappear to still qualify as motion marker.')
@click.option('--min-num-motion-markers', type=int, default=4, show_default=True, help='Minimum number of motion markers to consider a slice.')
@click.option('--chunk-selection', callback=parse_integers, default='', help='Chunk to select.')
@click.option('--max-movement', type=int, default=15, show_default=True, help='Maximum number of pixels a epicenter can  move from frame to next frame without being removed.')
@click.option('--interactive', is_flag=True, show_default=True, default=False, help='Enable interactive mode for motion marker selection.')
@click.option('--use-defaults', is_flag=True, show_default=True, default=False, help='Use default values for motion marker selection in interactive mode.')
@click.option('--do-not-run', is_flag=True, show_default=True, default=False, help='Only run the motion marker selection.')
@click.option('--combined', is_flag=True, show_default=True, default=True, help='Select MMs for all chunks combined.')
@click.option('--only-areas', is_flag=True, show_default=True, default=False, help='Only recompute the areas.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
@debug_handler()
def slice(dataset, n_slices, n_workers, threads_per_worker, processes, buffer, area_cutoff, max_ecc,
		  max_area, max_cv, zero_consecutive, zero_proportion, min_num_motion_markers, chunk_selection, max_movement,
		  interactive, use_defaults, do_not_run, combined, only_areas,
		  debug, debug_visual) -> None:
	""" Slice chromatophores into radial segments and track size. """
	from .source.slicing.slicing import slice

	if timeit:
		slice = timing_handler(timeit)(slice)
		
	cluster_args = {'processes': processes, 'n_workers': n_workers, 'threads_per_worker': threads_per_worker}
	debug_args = {'debug': debug, 'debug_visual': debug_visual}

	slice(dataset, n_slices, buffer, area_cutoff, max_ecc,
		  max_area, max_cv, zero_proportion, zero_consecutive,
		  min_num_motion_markers, chunk_selection, max_movement, interactive, use_defaults, do_not_run, combined, only_areas,
		  cluster_args, debug_args)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=-1, show_default=False, help='Chunk to analyse. If not set, analyse the whole dataset.')
@click.option('--n-slices', type=int, default=36, show_default=True, help='Number of slices to divide chromatophores into.')
@click.option('--area', is_flag=True, show_default=True, default=False, help='Analyse area of chromatophores.')
def ica(dataset, chunk, n_slices, area) -> None:
	""" Run Independent Component Analysis. """
	if area:
		from .source.ica.ica_areas import ica
	else:
		from .source.ica.ica_slices import ica
	if chunk == -1:
		chunk = None

	ica(dataset, chunk, n_slices)


@cli.command()
@click.argument('datasets', nargs=-1, type=click.Path(exists=True))
@click.option('-gs', '--grid-size', type=int, default=32, show_default=True,
			  help='Grid size for registration map.')
@click.option('-ps', '--patch-size', type=int, default=64, show_default=True,
			  help='Patch size for fine alignment.')
@click.option('-cgs', '--coarse-grid-size', type=int, default=128, show_default=True,
			  help='Grid size for coarse alignment.')
@click.option('-ie', '--initial-estimate', type=str, default='rotation', show_default=True,
			  help='Initial estimate method for alignment.')
@click.option('-ss', '--search-space', type=str,
			  default='512;2,0.35;0.035,None;None,None;None', show_default=True,
			  help='Search space for fine alignment.')
@click.option('-ce', '--clear-edge', type=int, default=40, show_default=True,
			  help='Number of pixels to clear from edge.')
@click.option('-ct', '--center-threshold', type=float, default=0.5, show_default=True,
			  help='Threshold for chromatophore center detection.')
@click.option('-mi', '--mask-inner', is_flag=True, default=False, show_default=True,
			  help='Use only inner chromatophores for mask.')
@click.option('-mdi', '--mask-dilation-iterations', type=int, default=5, show_default=True,
			  help='Number of dilation iterations for masking.')
@click.option('--mls-alpha', type=float, default=6.0, show_default=True,
			  help='Alpha parameter for moving least squares.')
@click.option('--ransac-tolerance', type=float, default=1.0, show_default=True,
			  help='Tolerance for RANSAC in fine alignment.')
@click.option('-d', '--debug', is_flag=True, default=False, show_default=True,
			  help='Enable debug mode.')
@click.option('-dv', '--debug-visual', is_flag=True, default=False, show_default=True,
			  help='Show debugging visualizations.')
@debug_handler()
def superstitch(datasets, grid_size, patch_size, coarse_grid_size, initial_estimate,
				search_space, clear_edge, center_threshold, mask_inner, mask_dilation_iterations,
				mls_alpha, ransac_tolerance, debug, debug_visual):
	"""
	Superstitch datasets together to create a super-dataset using manual alignment.
	
	Each input dataset must contain a queenframe and a cleanqueen (in group 'stitching').
	For each consecutive pair (dataset1→dataset2, dataset2→dataset3, …),
	the user is prompted to manually select corresponding points using ImagePointSelector.
	These manual alignments are then used (via chunkstitching) to compute dense registration maps.
	
	All datasets are warped into the coordinate system of the last (newest) dataset and averaged,
	yielding a merged superframe and superclean. Chromatophore ID mappings are computed between consecutive datasets.
	
	Example:
	  chromas superstitch /path/to/dataset1 /path/to/dataset2 /path/to/dataset3
	"""
	from .source.superstitching.superstitching import superstitching
	superstitching(dataset_paths=datasets,
					grid_size=grid_size,
					patch_size=patch_size,
					coarse_grid_size=coarse_grid_size,
					initial_estimate=initial_estimate,
					search_space=search_space,
					clear_edge=clear_edge,
					center_threshold=center_threshold,
					mask_inner=mask_inner,
					mask_dilation_iterations=mask_dilation_iterations,
					mls_alpha=mls_alpha,
					ransac_tolerance=ransac_tolerance,
					debug=debug,
					debug_visual=debug_visual)



#####################################################################################
#################### WORKFLOWS ######################################################
#####################################################################################

def option_to_decorator(option: click.Option):
	"""
	Convert a click.Option instance to a decorator by extracting its parameters.
	"""
	kwargs = {}
	if option.type is not None:
		kwargs["type"] = option.type
	if hasattr(option, "help") and option.help is not None:
		kwargs["help"] = option.help
	if option.default is not None:
		kwargs["default"] = option.default
	if option.required:
		kwargs["required"] = option.required
	if option.show_default:
		kwargs["show_default"] = option.show_default
	if option.multiple:
		kwargs["multiple"] = option.multiple
	if option.hidden:
		kwargs["hidden"] = option.hidden

	return click.option(*option.opts, **kwargs)


def add_options(options):
	"""
	A decorator that attaches a list of click options (as decorators) to a command.
	Only click.Option objects are converted; any non-option (e.g. click.Argument) is skipped.
	"""
	def _add_options(func):
		for option in reversed(options):
			if isinstance(option, click.Option):
				decorator = option_to_decorator(option)
				func = decorator(func)
		return func
	return _add_options


def get_params_for_task(task, kwargs):
	"""
	Given a click command (task) and a dict of all kwargs from the run command,
	return only those parameters that are defined for the task.
	"""
	task_option_names = {opt.name for opt in task.params if isinstance(opt, click.Option)}
	return {k: v for k, v in kwargs.items() if k in task_option_names}


@cli.command()
@click.argument('video_file', type=click.Path(exists=True))
@add_options(merge_task_options([chunk, segment, register, stitch, area, slice]))
def run(video_file, **kwargs):
	"""
	Run the full pipeline: chunk, segment, register, stitch, area, slice in order.
	
	All parameters from the underlying commands are available here.
	For example:
	
		chromas run /path/to/video.mp4 --output-name mydataset --focus-threshold 1.5 --n-slices 24

	The parameters are automatically distributed to each step.
	"""
	ctx = click.get_current_context()
	click.echo("Starting full pipeline run...")

	# --- Step 1: Chunk ---
	click.echo("Running chunk...")
	chunk_opts = get_params_for_task(chunk, kwargs)
	# Supply the required video_file argument
	chunk_opts["video_file"] = video_file
	dataset = ctx.invoke(chunk, **chunk_opts)
	if not dataset:
		click.secho("Chunking failed.", fg="red")
		return

	# --- Step 2: Segment ---
	click.echo("Running segment...")
	seg_opts = get_params_for_task(segment, kwargs)
	ctx.invoke(segment, dataset=dataset, **seg_opts)

	# --- Step 3: Register ---
	click.echo("Running register...")
	reg_opts = get_params_for_task(register, kwargs)
	ctx.invoke(register, dataset=dataset, **reg_opts)

	# --- Step 4: Stitch ---
	click.echo("Running stitch...")
	stitch_opts = get_params_for_task(stitch, kwargs)
	ctx.invoke(stitch, dataset=dataset, **stitch_opts)

	# --- Step 5: Area ---
	click.echo("Running area...")
	area_opts = get_params_for_task(area, kwargs)
	ctx.invoke(area, dataset=dataset, **area_opts)

	# --- Step 6: Slice ---
	click.echo("Running slice...")
	slice_opts = get_params_for_task(slice, kwargs)
	ctx.invoke(slice, dataset=dataset, **slice_opts)

	click.secho("Pipeline run completed successfully.", fg="green")


@cli.command(name="batch-run")
@click.argument('videos', nargs=-1, type=click.Path(exists=True))
@add_options(merge_task_options([chunk, segment, register, stitch, area, slice]))
def batch_run(videos, **kwargs):
	"""
	Run the full pipeline on multiple video files.
	
	Example:
		chromas batch-run vid1.mp4 vid2.mp4 vid3.mp4 --output-name mydataset --focus-threshold 1.5 --n-slices 24

	This command iterates over each provided video file and calls the 'run' command with the given parameters.
	"""
	ctx = click.get_current_context()
	if not videos:
		click.secho("No videos provided for batch-run.", fg="red")
		return

	for video in videos:
		click.echo(f"\nRunning pipeline for: {video}")
		# Invoke the run command for each video file.
		ctx.invoke(run, video_file=video, **kwargs)


#########################################################################################################################################################!
#################################### UTILITIES ##########################################################################################################!
#########################################################################################################################################################!
@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-s', '--start', type=int, default=0, show_default=True, help='Start frame to trim from.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End frame to trim to.')
def trim_frames(dataset, chunk, start, end):
	""" Trim frames from dataset. """
	from .source.tools.trim_frames import trim_frames
	trim_frames(dataset, chunk, start, end)
	click.secho('Frames trimmed.', fg='green')


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
def print(dataset):
	""" Print dataset information. """
	from .source.tools.print_dataset import print_dataset
	print_dataset(dataset)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
def status(dataset):
	""" Print dataset information. """
	from .source.tools.status_dataset import status_dataset
	status_dataset(dataset)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-ce', '--clear-edge', type=int, default=40, show_default=True, help='Number of pixels to clear from edge of image.')
@click.option('-mr', '--min-reprojection', type=float, default=0.5, show_default=True, help='Minimum reprojection score.')
def redo_queenframe(dataset, clear_edge, min_reprojection):
	""" Recompute the queenframe. Useful in case you exclude a chunk from analysis. """
	from .source.stitching.stitching import redo_queenframe

	redo_queenframe(dataset, clear_edge, min_reprojection)


@cli.command()
@click.argument('dataset', type=click.Path(exists=True))
def select_chroms(dataset):
	""" Select chromatophores to consider. Modify the cleanqueen accordingly. """
	from .source.tools.select_chroms import select_chroms
	select_chroms(dataset)


@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-n', '--nr-classes', type=int, default=2, show_default=True, help='Number of classes.')
@click.option('-d', '--debug', is_flag=True, help="Enable debug mode to print executed commands.")
@debug_handler()
def unify_training_data(directory, nr_classes, debug):
	""" Unify annotated training data. """
	from .source.training.unify_training_data import process_images_and_masks
	process_images_and_masks(directory, nr_classes, debug)


#########################################################################################################################################################!
####################################  PROCESS VIDEO FILES  ##############################################################################################!
#########################################################################################################################################################!
@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-s', '--start', type=int, help='Start time in seconds')
@click.option('-e', '--end', type=int, help='End time in seconds')
@click.option('-t', '--time', type=int, help='Duration in seconds')
@click.option('-o', '--output', type=click.Path(), help='Output file name')
@click.option('--no-interactive', is_flag=True, help='Disable interactive cropping')
@click.option('-x', type=int, help='x coordinate for cropping')
@click.option('-y', type=int, help='y coordinate for cropping')
@click.option('-dx', type=int, help='Width of the crop box')
@click.option('-dy', type=int, help='Height of the crop box')
def cut(input_file, start, end, time, output, no_interactive, x, y, dx, dy):
	"""Cut and/or crop video file. Cropping window can be specified interactively or by providing x, y, dx, dy.
	   Cut times can be specified by providing start, end or time (start + time = end).
	   If both start and end are provided, time will be ignored."""
	from .source.utils.video import cut_or_crop_video_interactive

	result = cut_or_crop_video_interactive(
		input_file, start, end, time, output, no_interactive, x, y, dx, dy
	)
	click.echo(f"Video processed successfully. Output: {result}")


#########################################################################################################################################################!
####################################  SHOW RESULTS  #####################################################################################################!
#########################################################################################################################################################!
@cli.group()
def show():
	""" Display results. """
	pass


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
def focus(ctx, dataset):
	from .source.chunking.chunking import show_focus
	show_focus(dataset)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-f', '--frame', type=int, default=0, show_default=True, help='Frame number to display.')
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
def segmentation(ctx, dataset, chunk, frame):
	from .source.segmentation.segmentation_neuralnet import show_segmentation
	show_segmentation(dataset, chunk, frame)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-p', '--peaks', type=bool, help='Color regions where `queenframe = 100%` in green.')
def masterframe(ctx, dataset, chunk, peaks):
	from .source.registration.registration import show_masterframe
	show_masterframe(dataset, chunk, peaks)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-p', '--peaks', type=bool, help='Color regions where `queenframe = 100%` in green.')
def queenframe(ctx, dataset, peaks):
	from .source.stitching.stitching import show_queenframe
	show_queenframe(dataset, peaks)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('--no-interactive', is_flag=True, show_default=True, default=False, help='Show only areas lines plot, without cleanqueen or interaction.')
def areas(ctx, dataset, chunk, no_interactive):
	from .source.areas.areas import show_areas
	show_areas(dataset, chunk, no_interactive)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-f', '--frame', type=int, default=0, show_default=True, help='Frame number to display.')
@click.option('-r', '--raw', is_flag=True, show_default=True, default=False, help='Just show cleanqueen, no overlay.')
@click.option('--id', type=int, default=None, show_default=True, help='ID of chromatophore to display.')
def cleanqueen(ctx, dataset, chunk, frame, raw, id):
	from .source.areas.areas import show_cleanqueen
	show_cleanqueen(dataset, chunk, frame, raw, id)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('--max-area-cutoff', type=int, default=10_000, show_default=True, help='Maximum area of chromatophore to consider.')
@click.option('--eccentricity-threshold', type=float, default=0.6, show_default=True, help='Threshold for eccentricity of chromatophore.')
@click.option('--max-area', type=int, default=3_000, show_default=True, help='Threshold of maximum area of chromatophore to qualify as motion_marker.')
@click.option('--max-cv', type=float, default=1.0, show_default=True, help='Threshold for coefficient of variation of chromatophore activity to qualify as motion_marker.')
def mm(ctx, dataset, chunk, eccentricity_threshold, max_area, max_cv, max_area_cutoff):
	from .source.slicing.slicing import show_motion_marker
	show_motion_marker(dataset, chunk, eccentricity_threshold, max_area, max_cv, max_area_cutoff)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=-1, show_default=False, help='Chunk to analyse. If not set, analyse the whole dataset.')
@click.option('-s', '--cluster-sizes', callback=parse_integers, default='',help='Minimum cluster sizes to consider.')
@click.option('-o', '--output-dir', type=click.Path(), default=None, show_default=True, help='Output directory for plots.')
@click.option('-r', '--radial', is_flag=True, show_default=True, default=False, help='Plot radial IC flowers for a random subset of chroms.')
@click.option('--show-cleanqueen', type=bool, default=False, show_default=True, help='Overlay cleanqueen.')
@click.option('--show-skeleton', type=bool, default=False, show_default=True, help='Overlay skeleton.')
@click.option('--show-lines', type=bool, default=False, show_default=True, help='Plot lines connecting chromatophores belonging to the same cluster.')
@click.option('--show-mm', type=bool, default=False, show_default=True, help='Plot motion markers.')
@click.option('--show-slices', type=bool, default=True, show_default=True, help='Plot labeled slices.')
@click.option('--show-ics', type=bool, default=False, show_default=True, help='Plot histogram of ICs per chrom.')
@click.option('--show-clustersize', type=bool, default=False, show_default=True, help='Plot histogram of clustersizes.')
def ica_cluster(ctx, dataset, chunk, cluster_sizes, output_dir, radial,
				show_cleanqueen, show_skeleton, show_lines, show_mm, show_slices, show_ics, show_clustersize) -> None:
	from .source.analysis.ica_slice_clustering import plot_slice_cluster
	
	if chunk == -1:
		chunk = None

	plot_slice_cluster(dataset, chunk, cluster_sizes, output_dir, radial, False, show_cleanqueen,
					   show_skeleton, show_lines, show_mm, show_slices, show_ics, show_clustersize)


@show.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
def reprojection_error(ctx, dataset):
	from .source.stitching.stitching import show_reprojection_error
	show_reprojection_error(dataset)


@show.command()
@click.pass_context
@click.argument('file_path', type=click.Path(exists=True))
def training_image(ctx, file_path):
	from .source.training.show_training_image import plot_image_mask_segmentation
	plot_image_mask_segmentation(file_path)


#######################################################################################################################################################!
#################################### ANALYSE RESULTS  #################################################################################################!
#######################################################################################################################################################!
@cli.group()
def analyse():
	""" Analyse results. """
	pass


@analyse.command()
@click.pass_context
@click.argument('stats', type=click.Choice(['areas', 'slices', 'ics']))
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=-1, show_default=False, help='Chunk to analyse. If not set, analyse the whole dataset.')
@click.option('-m', '--method', type=click.Choice(['affinitypropagation', 'hierarchiecal','hdbscan']), default='affinitypropagation', show_default=True, help='Clustering method to use.')
@click.option('-mt', '--max-tries', type=int, default=10, show_default=True, help='Maximum number of tries for clustering algorithm to converge.')
@click.option('-d', '--debug', is_flag=True, show_default=True, default=False, help='Print debugging info.')
@click.option('-dv', '--debug-visual', is_flag=True, show_default=True, default=False, help='Plot debugging info.')
# Affining Propagation kwargs:
@click.option('--damping', type=float, default=0.5, show_default=True, help='Damping factor for affinity propagation.')
@click.option('--max-iter', type=int, default=200, show_default=True, help='Maximum number of iterations for affinity propagation.')
@click.option('--convergence-iter', type=int, default=15, show_default=True, help='Number of iterations with no change to declare convergence.')
# HDSCAN kwargs:
@click.option('--min-cluster-size', type=int, default=5, show_default=True, help='Minimum number of samples in a cluster.')
@click.option('--max-cluster-size', type=int, default=None, show_default=True, help='Minimum number of samples in a cluster.')
@click.option('--min-samples', type=int, default=None, show_default=True, help='Number of samples in a neighbourhood for a point to be considered a core point.')
@click.option('--cluster-selection-epsilon', type=float, default=0.0, show_default=True, help='Radius of epsilon neighbourhood.')
@click.option('--cluster-selection-method', type=str, default='eom', show_default=True, help='Method to select clusters.')
@click.option('--alpha', type=float, default=1.0, show_default=True, help='Weighting factor that determines relative importance of min_samples and min_cluster_size.')
@click.option('--allow-single-cluster', type=bool, default=True, show_default=True, help='Allow single cluster.')
@click.option('--leaf-size', type=int, default=40, show_default=True, help='Leaf size of the KDTree.')
# Hierarchical kwargs:
@click.option('--criterion', type=str, default='distance', show_default=True, help='Criterion to use for clustering.')
# Other kwargs:
@click.option('--n-slices', type=int, default=36, show_default=True, help='Number of slices to divide chromatophores into.')
@debug_handler()
def cluster(ctx, stats, dataset, chunk, method, max_tries, debug, debug_visual, damping, max_iter, convergence_iter, min_cluster_size,
				max_cluster_size, min_samples, cluster_selection_epsilon, cluster_selection_method, alpha, allow_single_cluster,
				leaf_size, criterion, n_slices) -> None:
	
	if chunk == -1:
		chunk = None
	
	debug_args={'debug': debug, 'debug_visual': debug_visual}

	match method:
		case 'affinitypropagation':
			clustering_kwargs = {'damping': damping, 'max_iter': max_iter, 'convergence_iter': convergence_iter}
		case 'hdbscan':
			clustering_kwargs = {'min_cluster_size': min_cluster_size, 'max_cluster_size': max_cluster_size, 'min_samples': min_samples, 'cluster_selection_epsilon': cluster_selection_epsilon, 'cluster_selection_method': cluster_selection_method, 'alpha': alpha, 'allow_single_cluster': allow_single_cluster, 'leaf_size': leaf_size}
		case 'hierarchiecal':
			clustering_kwargs = {'criterion': criterion}

	match stats:
		case 'areas':
			from .source.analysis.areas_clustering import cluster_areas
			cluster_areas(dataset, chunk, method, clustering_kwargs, max_tries, debug_args)
		case 'slices':
			from .source.analysis.sliceareas_clustering import cluster_slice_areas
			cluster_slice_areas(dataset, chunk, method, clustering_kwargs, max_tries, debug_args)
		case 'ics':
			from .source.analysis.ica_slice_clustering import ica_slice_cluster        
			ica_slice_cluster(dataset, chunk, method, clustering_kwargs, max_tries, debug_args=debug_args, nr_slices=n_slices)


#######################################################################################################################################################!
####################################  GENERATE VISUALIZATION VIDEOS AND PLOTS #########################################################################!
#######################################################################################################################################################!
@cli.group()
def generate():
	""" Generate visualization videos. """
	pass

@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--fps', type=int, default=None, show_default=True, help='FPS of output video. If None, matches input video.')
@click.option('-s', '--start', type=int, default=None, show_default=True, help='Start of video in seconds.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End of video in seconds.')
def overlay_video(ctx, dataset, chunk, output, fps, start, end):
	from .source.segmentation.segmentation_neuralnet import generate_overlay_video
	generate_overlay_video(dataset, chunk, output, fps, start, end)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--fps', type=int, default=None, show_default=True, help='FPS of output video. If None, matches input video.')
@click.option('-s', '--start', type=int, default=None, show_default=True, help='Start of video in seconds.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End of video in seconds.')
def cleanqueen_video(ctx, dataset, chunk, output, fps, start, end):
	from .source.areas.areas import generate_cleanqueen_video
	generate_cleanqueen_video(dataset, chunk, output, fps, start, end)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--fps', type=int, default=None, show_default=True, help='FPS of output video. If None, matches input video.')
@click.option('-s', '--start', type=int, default=None, show_default=True, help='Start of video in seconds.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End of video in seconds.')
@click.option('-b', '--buffer', type=int, default=40, show_default=True, help='Buffer to remove from frame edge in cleanqueen.')
def center_video(ctx, dataset, chunk, output, fps, start, end, buffer) -> None:
	from .source.slicing.generate import generate_center_video
	generate_center_video(dataset, chunk, output, fps, start, end, buffer)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--fps', type=int, default=None, show_default=True, help='FPS of output video. If None, matches input video.')
@click.option('-s', '--start', type=int, default=None, show_default=True, help='Start of video in seconds.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End of video in seconds.')
@click.option('-b', '--buffer', type=int, default=40, show_default=True, help='Buffer to remove from frame edge in cleanqueen.')
@click.option('--interactive', is_flag=True, show_default=True, default=False, help='Choose chroms to display interactively.')
@click.option('--individual', is_flag=True, show_default=True, default=False, help='Generate videos of individual chromatophores.')
def slice_video(ctx, dataset, chunk, output, fps, start, end, buffer, interactive, individual) -> None:
	from .source.slicing.generate import generate_slice_video
	generate_slice_video(dataset, chunk, output, fps, start, end, buffer, interactive, individual)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--frame', type=int, default=0, show_default=True, help='Frame number to save as image.')
@click.option('-b', '--buffer', type=int, default=40, show_default=True, help='Buffer to remove from frame edge in cleanqueen.')
@click.option('--interactive', is_flag=True, show_default=True, default=False, help='Choose chroms to display interactively.')
@click.option('--individual', is_flag=True, show_default=True, default=False, help='Generate videos of individual chromatophores.')
def slice_frame(ctx, dataset, chunk, frame, output, buffer, interactive, individual) -> None:
	from .source.slicing.generate import generate_slice_frame
	generate_slice_frame(dataset, chunk, frame, output, buffer, interactive, individual)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=-1, show_default=False, help='Chunk to analyse. If not set, analyse the whole dataset.')
@click.option('-s', '--cluster-sizes', callback=parse_integers, default='',help='Minimum cluster sizes to consider.')
@click.option('-o', '--output-dir', type=click.Path(), default=None, show_default=True, help='Output directory for plots.')
@click.option('-r', '--radial', is_flag=True, show_default=True, default=False, help='Plot radial IC flowers for a random subset of chroms.')
def ica_slice_cluster(ctx, dataset, chunk, cluster_sizes, output_dir, radial) -> None:
	from .source.analysis.ica_slice_clustering import plot_slice_cluster
	
	if chunk == -1:
		chunk = None

	plot_slice_cluster(dataset, chunk, cluster_sizes, output_dir, radial, generate=True)


@generate.command()
@click.argument('video_path', type=click.Path(exists=True))
@click.option('-f', '--frame', type=int, default=0, show_default=True, help='Frame number to save as image.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
def frame(video_path, frame, output):
	""" Save a frame from a video as an image. """
	from .source.utils.video import save_frame
	save_frame(video_path, frame, output)


@generate.command()
@click.pass_context
@click.argument('dataset', type=click.Path(exists=True))
@click.option('-c', '--chunk', type=int, default=0, show_default=True, help='Chunk to display.')
@click.option('-o', '--output', type=click.Path(), default=None, show_default=True, help='Optional output file.')
@click.option('-f', '--fps', type=int, default=None, show_default=True, help='FPS of output video. If None, matches input video.')
@click.option('-s', '--start', type=int, default=None, show_default=True, help='Start of video in seconds.')
@click.option('-e', '--end', type=int, default=None, show_default=True, help='End of video in seconds.')
@click.option('-b', '--buffer', type=int, default=40, show_default=True, help='Buffer to remove from frame edge in cleanqueen.')
@click.option('--interactive', is_flag=True, show_default=True, default=False, help='Choose chroms to display interactively.')
@click.option('--individual', is_flag=True, show_default=True, default=False, help='Generate videos of individual chromatophores.')
def videos(ctx, dataset, chunk, output, fps, start, end, buffer, interactive, individual) -> None:
	from .source.segmentation.segmentation_neuralnet import generate_overlay_video
	generate_overlay_video(dataset, chunk, output, fps, start, end)

	from .source.slicing.slicing import generate_center_video
	generate_center_video(dataset, chunk, output, fps, start, end, buffer)

	from .source.slicing.slicing import generate_slice_video
	generate_slice_video(dataset, chunk, output, fps, start, end, buffer, interactive, individual)


####################################################################################################################################################!
####################################### TEST FUNCTIONS  ############################################################################################!
####################################################################################################################################################!
@cli.group()
def test():
	""" Run test runs. """
	pass

@test.command()
@click.pass_context
@click.argument('video_path', type=click.Path(exists=True))
@click.option('-ma', '--model-architecture', type=str, default='fcn_resnet50', show_default=True, help='Model architecture to use for segmentation.')
@click.option('-mw', '--model-weights', type=click.Path(exists=True), default='/gpfs/laur/data/ukrowj/models/2_class_chrom_segmentation/fcn_resnet50_400_best_model.pth', show_default=True, help='Path to trained Neural Network classifier.')
@click.option('-f', '--frame-idx', type=int, default=0, show_default=True, help='Frame index to segment.')
@click.option('-ov', '--overlay', type=bool, default=True, show_default=True, help='Overlay segmentation on video.')
def seg(ctx, video_path, model_architecture, model_weights, frame_idx, overlay):
	from .source.segmentation.segmentation_neuralnet import test_segmentation
	test_segmentation(video_path, model_architecture, model_weights, frame_idx, overlay)


####################################################################################################################################################!
####################################### RUN MAIN FUNCTION  #########################################################################################!
####################################################################################################################################################!

if __name__ == '__main__':
	cli()
