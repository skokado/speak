#include <Python.h>

static PyObject* my_abs(PyObject* self, PyObject* args) {
    long value;

    if (!PyArg_ParseTuple(args, "l", &value)) {
        return NULL;
    }

    long result = Py_ABS(value);
    return PyLong_FromLong(result);
}

static PyMethodDef MyModuleMethods[] = {
    {"my_abs", my_abs, METH_VARARGS, "Return the absolute value of a number"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    "",
    -1,
    MyModuleMethods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
