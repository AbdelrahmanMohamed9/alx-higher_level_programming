#ifndef _LIST_H_
#define _LIST_H_

#include <stdlib.h>

/**
 * struct listint_s - That Is The Singly Linked List.
 * @n: int.
 * @next:That Is The Point To Next Node.
 *
 *
 * Description:That Is The Singly Linked List Node Structure.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;


size_t print_listint(const listint_t *);
listint_t *add_nodeint(listint_t **, const int);
void free_listint(listint_t *);
int check_cycle(listint_t *);


#endif
