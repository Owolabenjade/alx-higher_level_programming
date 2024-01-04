#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

/**
 *struct listint_s - singly linked list
 *@n: integer
 *@next: points to the next node
 *
 *Description: singly linked list node structure
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Function prototypes */
listint_t *insert_node(listint_t **head, int number);
void print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif /* LISTS_H */
