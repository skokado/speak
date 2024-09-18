## Requirements

You need libpython dev package (= `Python.h`; Python/C API) for develop/building from C/C++ code

e.g.

```sh
$ sudo apt install -y libpython3.12-dev
```

## Build

```sh
python3 -m pip install .
```

```python
>>> import mymodule
>>> mymodule
<module 'mymodule' from '/.../site-packages/mymodule-1.0-py3.12-linux-x86_64.egg/mymodule.cpython-312-x86_64-linux-gnu.so'>

>>> mymodule.my_abs(-42)
42
>>> mymodule.my_abs(42)
42
```
