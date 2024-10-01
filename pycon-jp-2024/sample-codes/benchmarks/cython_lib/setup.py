from setuptools import Extension, setup
import sys

from Cython.Build import cythonize


setup(
    name='cython_lib',
    ext_modules=cythonize("cython_lib.pyx"),
)
