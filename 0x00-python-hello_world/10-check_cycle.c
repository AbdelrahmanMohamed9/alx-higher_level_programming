#include "lists.h"

/**
 * check_cycle - Determine whether a singly linked list contains a loop
 * @list: The Pointer to the first node of
 *	a singly linked list of type listint_t
 * Return: in case there is no loop return 0. otherwise return 1 .
 */
int check_cycle(listint_t *list)
{
	listint_t *d1 = NULL, *d2 = NULL;

	if (!list)
		return (0);

	d1 = list;
	d2 = list;
	while (d1 && d2 && d2->next)
	{
		d1 = d1->next;
		d2 = d2->next->next;
		if (d1 == d2)
			return (1);
	}
	return (0);
}
