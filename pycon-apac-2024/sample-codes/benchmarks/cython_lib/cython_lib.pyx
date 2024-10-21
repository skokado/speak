def eratosthenes(int limit) -> list[bool]:
    cdef int i, p
    cdef list prime_flags = [True for _ in range(limit + 1)]  # Use a list of Python

    p = 2
    while p * p <= limit:
        if prime_flags[p]:
            for i in range(p * p, limit + 1, p):
                prime_flags[i] = 0
        p += 1
    
    cdef list prime_numbers = []
    for p in range(2, limit):
        if prime_flags[p]:
            prime_numbers.append(p)
    
    return prime_numbers


def get_primes(int max) -> list[int]:
    cdef int i, n
    cdef list primes = [2]

    for n in range(3, max + 1, 2):
        i = 3
        while i * i <= n:
            if n % i == 0:
                break
            i += 2
        else:
            primes.append(n)

    return primes
