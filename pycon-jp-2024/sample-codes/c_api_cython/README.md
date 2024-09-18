## Requirements

You need libpython dev package (= `Python.h`; Python/C API) for develop/building with Cython

Please install OpenMP in order to optimize code performance to the greatest extent possible for parallel processing

e.g.

```sh
$ sudo apt update
$ sudo apt install -y libpython3.12-dev clang libomp-dev
```

## Build

```sh
python3 -m pip install . --force-reinstall --compile
```

```python
>>> import cymodule
>>> cymodule
<module 'cymodule' from '/.../site-packages/cymodule.cpython-312-x86_64-linux-gnu.so'>

>>> cymodule.my_abs(-1)
1
```

Compare performance of sum_sequence

```sh
$ python benchmark.py
...
N_MAX=500,array_length=100000

Duration:
py_l2norm                : 13.678 sec
cymodule.l2norm          : 0.037 sec
cymodule.l2norm_with_gil : 1.072 sec
```
