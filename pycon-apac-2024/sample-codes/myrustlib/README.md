# myrustlib

## How to run

```sh
$ maturin develop --release
$ python3 main.py
```

## How to implement

A light tutorial to use Rust codes as a Python library

Steps:

```sh
$ # Create and activate venv
$ pip3 install maturin

$ # Init project workspace
$ mkdir myrustlib
$ cd myrustlib
$ maturin init -b pyo3
$ # Implement src/lib.rs
```
