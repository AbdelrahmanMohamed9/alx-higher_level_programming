#include "lists.h"

/**
 * insert_node - Add a node to a linked list in ascending order.
 * @head: The first node of a linked list.
 * @number: The number that is going to be inserted or added to a data structure.
 * Return: The memory location or pointer to the
 *	newly created node in a data structure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev = *head;

	if (!new)
		return (0);

	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (prev->next)
	{
		if ((prev->next)->n >= number)
		{
			new->next = prev->next;
			prev->next = new;
			return (new);
		}
		prev = prev->next;
	}

	new->next = NULL;
	prev->next = new;
	return (new);
}
