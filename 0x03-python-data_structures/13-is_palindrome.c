#include "lists.h"

/**
 * reverse_list - reverse linked list
 * @head: head of linked list
 * Return: reversed list;
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *tmp = NULL;

	if (head == NULL)
		return (NULL);

	if (!head->next)
	{
		add_nodeint_end(&tmp, head->n);
		return (tmp);
	}

	tmp = reverse_list(head->next);
	add_nodeint_end(&tmp, head->n);

	return (tmp);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to first linked list
 * Return: 1 if palindrome 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *reversed = NULL, *my_list = *head;

	if (*head == NULL)
		return (1);
	/*reverse a copy of list*/
	reversed = reverse_list(my_list);
	temp = reversed;

	/*compare reversed list and list: if same palindrome*/
	while (my_list)
	{
		if (my_list->n != reversed->n)
		{
			free_listint(temp);
			return (0);
		}
		my_list = my_list->next;
		reversed = reversed->next;
	}

	free_listint(temp);
	return (1);
}
