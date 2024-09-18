# myrustlib

## How to run

```sh
$ maturin develop --release
$ python3 main.py
```

## How to implement

RustコードをPythonライブラリとして利用するための簡単なチュートリアル

このプロジェクトの初期化から完成までのステップ

```sh
$ # Create and activate venv
$ pip3 install maturin

$ # Init project workspace
$ mkdir myrustlib
$ cd myrustlib
$ maturin init -b pyo3
$ # Implement src/lib.rs
```
