#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to first linked list
 * Return: 1 if palindrome 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *reversed = NULL, *my_list = *head;
	int i = 0, j = 0;

	if (*head == NULL)
		return (1);
	/*find list length*/
	for (i = 0; my_list; i++)
		my_list = my_list->next;
	/*reverse a copy of list*/
	my_list = *head;
	while (my_list)
	{
		while (j < i - 1)
		{
			my_list = my_list->next;
			j++;
		}
		add_nodeint_end(&temp, my_list->n);
		my_list = *head;
		if (i == 1)
			break;
		i -= 1, j = 0;
	}
	reversed = temp;

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
