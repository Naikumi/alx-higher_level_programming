#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * pal - compares start and end of position
 * @head: the linked list
 * @end: end of the list
 *
 * Return: 1 on success, 0 false
 */
int pal(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pal(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the linked list
 * Return: 1 true, 0 false
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (pal(head, *head));
}
