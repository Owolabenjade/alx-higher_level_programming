fndef LISTS_H
#define LISTS_H

typedef struct listinit_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
