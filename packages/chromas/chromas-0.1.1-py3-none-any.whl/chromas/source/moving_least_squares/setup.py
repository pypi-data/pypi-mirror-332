from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

ext_modules=[
        Extension("moving_least_squares", \
                sources=['src/moving_least_squares.pyx'], \
                include_dirs=[np.get_include()])
]

setup(name='moving_least_squares',
        version='1.1.0',
        description='Warping library',
        author='Philipp Huelsdunk',
        ext_modules=cythonize(ext_modules, language_level = "3"))

