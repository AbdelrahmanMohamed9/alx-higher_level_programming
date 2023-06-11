#include "lists.h"

/**
 * reverse - Reverse the order of the second half
 *	of the list while maintaining its meaning.
 *
 * @h_r: The first element of the second half.
 * Return: nothing to  return
 */
void reverse(listint_t **h_r)
{
	listint_t *prev, *curr, *next;

	prev = NULL;
	curr = *h_r;
	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*h_r = prev;
}

/**
 * compare - that will Compare each integer in the list
 *
 * @h1: he first element of the first half.
 * @h2: The first element of the second portion.
 * Return: 1 if they are equal, otherwise return 0.
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1, *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (!tmp1 && !tmp2)
		return (1);

	return (0);
}

/**
 * is_palindrome - Determine if a singly linked list is a palindrome.
 *
 * @head: A pointer to the beginning of the list.
 * Return: 1 if the list is a palindrome, otherwise return 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int ip;

	slow = fast = prev_slow = *head;
	middle = NULL;
	ip = 1;
	if (*head && (*head)->next)
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		ip = compare(*head, scn_half);
		if (middle)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (ip);
}
