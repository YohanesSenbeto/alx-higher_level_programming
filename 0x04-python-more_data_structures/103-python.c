#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 *print_python_list-print info about pytho lits
 *@p:a pyobjec list obj
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    const char *type;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);

        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
    }
}
/**
 *print_python_bytes-print info about python byte
 *@p:a pyobjec byte obj
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *bytes;

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    if (!bytes)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", (char *)bytes);

    Py_ssize_t print_size = (size > 10) ? 10 : size;

    printf("  first %zd bytes: ", print_size);
    for (i = 0; i < print_size; i++)
    {
        printf("%02hhx", bytes[i]);
        if (i == (print_size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
