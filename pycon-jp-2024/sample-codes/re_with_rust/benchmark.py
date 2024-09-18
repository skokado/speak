import re
from timeit import timeit

import replacer

"""
引用元 https://gihyo.jp/article/2023/07/monthly-python-2307#ghe5tVmOyS
"""

# 引数で指定された正規表現を使用して、テキストを置換する関数
def replace_with_pattern(pattern, text, replacement):
    return re.sub(pattern, replacement, text)


if __name__ == "__main__":
    pattern = r"\d+"  # 正規表現パターン
    text = "Hello01Python23Rust45with678maturin"  # 置換対象文字列
    replacement = "-"  # 置換する文字列

    loop = 100  # 繰り返し実行回数

    # 本スクリプト内のPython関数を実行
    p_res = timeit(lambda: replace_with_pattern(pattern, text, replacement), number=loop)
    p_time = p_res / loop * 1_000_000  # 1回あたりの平均実行時間をマイクロ秒で計算
    print(f"Python Avg:\t{p_time:.2f} μs/call")

    # Pythonバインディングによる実行
    r_res = timeit(lambda: replacer.replace_with_pattern(pattern, text, replacement), number=loop)
    r_time = r_res / loop * 1_000_000  # 1回あたりの平均実行時間をマイクロ秒で計算
    print(f"Rust   Avg:\t{r_time:.2f} μs/call")
