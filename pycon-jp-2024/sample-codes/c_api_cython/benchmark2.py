import random
import timeit

import numpy as np

import cymodule


def init_array(length: int) -> np.ndarray:
    return np.array([
        round(random.random() * 100, 2)
        for _ in range(length)
    ])


repeat = 4

print("n,duration")
for exp in range(3, 7 + 1):
    n = pow(10, exp)
    arr = init_array(n)

    dur = timeit.timeit(lambda: cymodule.l2norm(arr), number=repeat)
    dur = round(dur / repeat, 4)
    print(f"{n},{dur}")
