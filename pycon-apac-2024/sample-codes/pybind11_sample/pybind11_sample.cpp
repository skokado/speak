// pybind11_sample.cpp
#include <pybind11/pybind11.h>

namespace py = pybind11;

int my_abs(int x) {
    return std::abs(x);
}

PYBIND11_MODULE(pybind11_sample, m) {
    m.def("abs", &my_abs, "PyBin11 sample");
}
