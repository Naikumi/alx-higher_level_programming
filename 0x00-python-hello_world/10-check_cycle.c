#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *loop1 = list;
	listint_t *loop2 = list;

	if (!list)
		return (0);
	while (loop1 && loop2 && loop2->next)
	{
		loop1 = loop1->next;
		loop2 = loop2->next->next;
		if (loop1 == loop2)
			return (1);
	}
	return (0);
}
