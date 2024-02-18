#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *obj;

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n",
           size, ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n  trying string: %s\n", size, PyBytes_AsString(p));
    printf("  first %ld bytes: ", (size < 10 ? size + 1 : 10));
    str = PyBytes_AsString(p);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x%c", str[i] & 0xff, i == 9 || i + 1 == size ? '\n' : ' ');
    }
}

/**
 * print_python_float - Prints some basic info about Python float objects
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
