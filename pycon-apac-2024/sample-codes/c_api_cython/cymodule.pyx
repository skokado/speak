from cython.parallel cimport prange
cimport cython
from libc.math cimport sqrt


cdef extern from "Python.h":
    cdef int Py_ABS(int x)

def my_abs(int x):
    return Py_ABS(x)


"""
Multi thread process sample without GIL
See also: https://cython.readthedocs.io/en/latest/src/tutorial/parallelization.html#reductions
"""

@cython.boundscheck(False)
@cython.wraparound(False)
def l2norm(double[:] x):
    cdef double total = 0
    cdef Py_ssize_t i

    for i in prange(x.shape[0], nogil=True):
        total += x[i]*x[i]

    return sqrt(total)


@cython.boundscheck(False)
@cython.wraparound(False)
def l2norm_with_gil(double[:] x):
    total = 0

    for i in range(x.shape[0]):
        total += x[i]*x[i]

    return sqrt(total)
