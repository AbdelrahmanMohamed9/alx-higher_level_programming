#include <Python.h>

/**
 * print_python_bytes - Displays byte data
 *
 * @p: Python data structure or Python variable.
 * Return: void return a value.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int sz, n, lmt;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  the [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	sz = ((PyVarObject *)(p))->ob_sz;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  the size: %ld\n", sz);
	printf("  the trying string: %s\n", str);

	if (sz >= 10)
		lmt = 10;
	else
		lmt = sz + 1;

	printf("  the first %ld bytes:", lmt);

	for (n = 0; n < lmt; n++)
		if (str[n] >= 0)
			printf(" %02x", str[n]);
		else
			printf(" %02x", 256 + str[n]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Displays decimal number data or
 *	prints floating-point values.
 *
 * @p: Python data structure or Python variable.
 * Return: void return a value.
 */
void print_python_float(PyObject *p)
{
	double vl;
	char *nz;

	setbuf(stdout, NULL);
	printf("the [.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  the [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	vl = ((PyFloatObject *)(p))->ob_fvl;
	nz = PyOS_double_to_string(vl, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  the value: %s\n", nz);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Displays array data or prints
 *	information about a list variable.
 *
 * @p: Python data structure or Python variable.
 * Return: void return a value.
 */
void print_python_list(PyObject *p)
{
	long int sz, n;
	PyListObject *lst;
	PyObject *oj;

	setbuf(stdout, NULL);
	printf("the [*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  the [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	sz = ((PyVarObject *)(p))->ob_sz;
	lst = (PyListObject *)p;

	printf("the [*] Size of the Python List = %ld\n", sz);
	printf("the [*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < sz; n++)
	{
		oj = lst->ob_item[n];
		printf("the Element %ld: %s\n", n, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(oj))
			print_python_bytes(oj);
		if (PyFloat_Check(oj))
			print_python_float(oj);
	}
	setbuf(stdout, NULL);
}
