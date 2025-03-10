""" Decorators for handling errors, debugging, timing, and convergence warnings. """

import functools
import time
import traceback
import warnings
from functools import wraps

import click
from dask.distributed import Client, LocalCluster
from sklearn.exceptions import ConvergenceWarning

from rich.console import Console
from rich.traceback import Traceback

console = Console()

def error_handler(task: str = 'Task', cluster: bool = True):
	"""
	A decorator to wrap functions in a try-except block and handle exceptions gracefully.

	Args:
		cluster (bool): Whether to set up and clean up a Dask cluster and client.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			use_cluster = cluster  # Avoid reusing the outer cluster variable
			_client, _cluster = None, None  # Ensure these are defined early
			try:
				if use_cluster:
					if 'cluster_args' in kwargs and kwargs['cluster_args'] is not None:
						_cluster = LocalCluster(**kwargs['cluster_args'])
						_client = Client(_cluster)
						click.secho(f'Dashboard: {_client.dashboard_link}', fg='blue')
						click.launch(_client.dashboard_link)
					else:
						use_cluster = False
				# Call the original function
				retval = func(*args, **kwargs)
			except Exception as e:
				if use_cluster:
					_client.close()
					_cluster.close()
				# Instead of printing a raw traceback, we use Rich:
				console.print(f"[bold red]\n\n--------> Error in {task}:[/bold red]")
				tb = Traceback.from_exception(type(e), e, e.__traceback__, show_locals=True)
				console.print(tb)
				console.print(f"[bold red]\n\n{task} failed![/bold red]")
				return False, None
			else:
				if use_cluster:
					_client.close()
					_cluster.close()
				click.secho(f"\n{task} complete.", fg='green', bold=True)
				return retval
				
		return wrapper
	return decorator


def debug_handler():
	""" Decorator for debugging function calls. """
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			ctx = click.get_current_context()
			# Check if debug or debug_visual is enabled
			debug_enabled = kwargs.get('debug', False) or kwargs.get('debug_visual', False)
			if debug_enabled:
				# Extract command name
				command_name = ctx.info_name or "[Unknown Command]"
				click.secho(f"\nDebug Info for Command: {command_name}", fg="yellow", italic=True, bold=True)
				click.secho("Arguments:", fg="yellow", italic=True)
				# Print positional arguments
				for arg_name, arg_value in zip(ctx.command.params, args):
					click.secho(f"    {arg_name.name}:	{arg_value}", fg="yellow", italic=True)
				click.secho("Options:", fg="yellow", italic=True)
				# Print keyword arguments
				for key, value in kwargs.items():
					click.secho(f"    {key}:	{value}", fg="yellow", italic=True)

			# Call the original function
			return f(*args, **kwargs)
		return wrapper
	return decorator


def timing_handler(timeit):
	""" Decorator for timing function calls.

	Args:
		timeit (bool): Whether to time the function call.

	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			if timeit:
				start_time = time.time()
			result = func(*args, **kwargs)
			if timeit:
				elapsed_time = time.time() - start_time
				click.echo(f'\n\nruntime: {elapsed_time} s.')
			return result
		return wrapper
	return decorator


def convergence_handler(func, max_tries: int = 5):
	"""
	Decorator for handling convergence warnings in clustering algorithms by
	converting them to exceptions and retrying.

	Args:
		func (function): The function to wrap.
		max_tries (int): The maximum number of attempts to try before 
						 raising a ConvergenceWarning.

	Raises:
		ConvergenceWarning: If the function could not converge after max_tries attempts.
	"""
	def wrapper(*args, **kwargs):
		count = 0
		
		while count < max_tries:
			# Create a local warning context so that 
			# ConvergenceWarning inside the function is raised as an exception.
			with warnings.catch_warnings():
				# Turn ConvergenceWarning into an exception
				warnings.simplefilter("error", ConvergenceWarning)
				
				try:
					return func(*args, **kwargs)
				except ConvergenceWarning:
					count += 1
					continue

		# If we reach here, it means the function still didn't converge after max_tries
		method = kwargs.get("method", func.__name__)
		raise ConvergenceWarning(f'{method} could not converge after {max_tries} attempts.')
	return wrapper
