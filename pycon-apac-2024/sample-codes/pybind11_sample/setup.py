from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "pybind11_sample",
        ["pybind11_sample.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="pybind11_sample",
    version="1.0",
    description="A simple example module using PyBind11",
    ext_modules=ext_modules,
)
