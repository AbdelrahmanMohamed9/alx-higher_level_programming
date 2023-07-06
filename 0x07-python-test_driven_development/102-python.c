#include "Python.h"

/**
 * print_python_string - This is a function that prints
 *	information about Python strings
 * @p: A Python string object represented as a PyObject.
 */
void print_python_string(PyObject *p)
{
	char *ssr;
	long int len;

	fflush(stdout);
	printf("[.] str object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" that [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)(p))->len;
	ssr = PyUnicode_AsWideCharString(p, &len);
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" the type: compact ascii\n");
	else
		printf(" the type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", ssr);
}
