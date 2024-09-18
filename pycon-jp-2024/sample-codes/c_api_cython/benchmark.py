import math
import random
import time

import numpy as np
from tqdm import tqdm

import cymodule


def py_l2norm(array: np.ndarray) -> float:
    double_total = 0
    for c in array:
        double_total += c ** 2

    return math.sqrt(double_total)


def init_array(length: int) -> np.ndarray:
    return np.array([
        round(random.random() * 100, 2)
        for _ in range(length)
    ])


if __name__ == "__main__":
    N_MAX = 500

    array_length = 100_000
    arr = init_array(array_length)

    print("--- 1. py_l2norm")
    start = time.time()
    for i in tqdm(range(N_MAX)):
        py_l2norm(arr)
    time_py = round(time.time() - start, 3)

    print("--- 2. cymodule.l2norm")
    start = time.time()
    for i in tqdm(range(N_MAX)):
        cymodule.l2norm(arr)
    time_cy = round(time.time() - start, 3)

    print("--- 3. cymodule.l2norm_with_gil")
    start = time.time()
    for i in tqdm(range(N_MAX)):
        cymodule.l2norm_with_gil(arr)
    time_cy_gil = round(time.time() - start, 3)

    print(f"{N_MAX=},{array_length=}")
    print("\nDuration:")
    print(f"py_l2norm                : {time_py} sec")
    print(f"cymodule.l2norm          : {time_cy} sec")
    print(f"cymodule.l2norm_with_gil : {time_cy_gil} sec")
