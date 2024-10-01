from setuptools import Extension, setup
import sys

from Cython.Build import cythonize


if sys.platform.startswith("win"):
    openmp_arg = '/openmp'
else:
    openmp_arg = '-fopenmp'


ext_modules = [
    Extension(
        "*",
        ["cython_lib.pyx"],
        extra_compile_args=[openmp_arg],
        extra_link_args=[openmp_arg],
    )
]


setup(
    name='cython_lib',
    ext_modules=cythonize(ext_modules),
)
