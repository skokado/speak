# setup.py
from setuptools import setup, Extension

module = Extension(
    "mymodule",
    sources=["mymodule.cpp"],
    language="c++",
)

setup(
    name="mymodule",
    version="1.0",
    description="A simple example module",
    ext_modules=[module],
)
