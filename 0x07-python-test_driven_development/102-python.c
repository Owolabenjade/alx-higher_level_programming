#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: PyObject string object.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    const char *string = NULL;
    int is_ascii = 0;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        is_ascii = 1;

    string = PyUnicode_AsUTF8AndSize(p, &length);
    if (!string)
    {
        PyErr_Clear();
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  type: %s\n", is_ascii ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %s\n", string);
}
