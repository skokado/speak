import csv
import timeit
import sys


def eratosthenes(limit: int) -> list[int]:
    prime_flags: list[bool] = [True for _ in range(limit + 1)]
    p = 2
    while p ** 2 <= limit:
        if prime_flags[p]:
            for i in range(p ** 2, limit + 1, p):
                prime_flags[i] = False
        p += 1
    primes: list[int] = [p for p in range(2, limit) if prime_flags[p]]
    return primes


def get_primes(max: int) -> list[int]:
    # n以下の素数一覧を返す愚直な実装
    primes = [2]

    for n in range(3, max + 1, 2):
        i = 3
        while i * i <= n:
            if n % i == 0:
                break
            i += 2
        else:
            primes.append(n)

    return primes


"""
Measure duration for each benchmarks, implementations (Python/Cython/Rust)
and output avg times.
"""
import cython_lib
import rust_lib


def benchmark_eratosthenes(repeat: int = 1):
    print("--- Eratosthenes")

    results = []
    """results:
    n,Python,Cython,Rust
    1000,...,
    10000,...,
    """

    for exp in range(3, 8 + 1):
        print(f"{exp=}")
        n = pow(10, exp)

        time_py = timeit.timeit(lambda: eratosthenes(n), number=repeat)
        time_py = round(time_py / repeat, 2)

        time_cy = timeit.timeit(lambda: cython_lib.eratosthenes(n), number=repeat)
        time_cy = round(time_cy / repeat, 2)

        time_rs = timeit.timeit(lambda: rust_lib.eratosthenes(n), number=repeat)
        time_rs = round(time_rs / repeat, 2)

        results.append([n, time_py, time_cy, time_rs])

    writer = csv.writer(sys.stdout)
    writer.writerow(["n", "Python", "Cython", "Rust"])
    writer.writerows(results)


def benchmark_get_primes(repeat: int = 1):
    print("--- Get Primes")

    results = []
    """results:
    n,Python,Cython,Rust
    1000,...,
    10000,...,
    """

    for exp in range(3, 7 + 1):
        print(f"{exp=}")
        n = pow(10, exp)

        time_py = timeit.timeit(lambda: get_primes(n), number=repeat)
        time_py = round(time_py / repeat, 2)

        time_cy = timeit.timeit(lambda: cython_lib.get_primes(n), number=repeat)
        time_cy = round(time_cy / repeat, 2)

        time_rs = timeit.timeit(lambda: rust_lib.get_primes(n), number=repeat)
        time_rs = round(time_rs / repeat, 2)

        results.append([n, time_py, time_cy, time_rs])

    writer = csv.writer(sys.stdout)
    writer.writerow(["n", "Python", "Cython", "Rust"])
    writer.writerows(results)


if __name__ == "__main__":
    benchmark_eratosthenes()
    print()
    benchmark_get_primes()
