from setuptools import Extension, setup
import sys

from Cython.Build import cythonize

"""
Compile with openmp option
See also:
https://cython.readthedocs.io/en/latest/src/tutorial/parallelization.html#compilation
"""

if sys.platform.startswith("win"):
    openmp_arg = '/openmp'
else:
    openmp_arg = '-fopenmp'


ext_modules = [
    Extension(
        "*",
        ["*.pyx"],
        extra_compile_args=[openmp_arg],
        extra_link_args=[openmp_arg],
    )
]


setup(
    name='cymodule',
    ext_modules=cythonize(ext_modules),
)
