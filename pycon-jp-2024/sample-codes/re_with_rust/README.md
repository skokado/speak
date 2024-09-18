# re_with_rust

Pythonの標準モジュール re と Rust の正規表現処理の性能比較をするサンプル

```sh
$ cd re_with_rust
$ pip3 install .

$ python3 benchmark.py 
Python Avg:     3.17 μs/call
Rust Avg:       79.64 μs/call
```

- Python-Rust間のオーバーヘッド
    - Pythonで処理負荷が低いものをRust化してもメリットが出ないことがある
    - 比較的大きいオブジェクトのやりとりは、オーバーヘッドを考慮して実装する必要がある
- CPUバウンドな処理が多い場合にはRustの恩恵を受けられる可能性が高い
- IOバウンドな処理に採用してもメリットが出ないことがある
- IOバウンドな処理＋その後の処理負荷を考慮して検討する

引用元: [PythonとRustの融合：PyO3/maturinを使ったPythonバインディングの作成入門 | gihyo.jp](https://gihyo.jp/article/2023/07/monthly-python-2307#ghe5tVmOyS)
