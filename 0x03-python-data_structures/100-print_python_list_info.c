#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p) {
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));

       fflush(stdout);
}
