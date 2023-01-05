#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int data;
	struct person* next;
} person;

person* first;
person* last;

void push(int data);
person* Josephuspop(int k, person* nextK);

int main(void) {
	
	int N, K;

	scanf("%d %d", &N, &K);

	first = (person*)malloc(sizeof(person));
	first = NULL;

	last = (person*)malloc(sizeof(person));
	last = NULL;

	for (int i = 0; i < N; i++) {
		push(i + 1);
	}
	last->next = first;

	printf("<");
	first = Josephuspop(K, first);
	for (int i = 1; i < N; i++) {
		printf(", ");
		first = Josephuspop(K, first);
	}
	printf(">");

	return 0;
}

void push(int data) {
	person* node = (person*)malloc(sizeof(person));
	node->data = data;

	if (first == NULL) {
		node->next = NULL;
		first = node;
		last = node;
	}
	else {
		last->next = node;
		last = node;
	}
	
}

person* Josephuspop(int k, person* nextK) {
	person* cur = nextK;
	person* temp = cur;
	for (int i = 1; i < k; i++) {
		temp = cur;
		cur = cur->next;
	}
	printf("%d", cur->data);
	temp->next = cur->next;
	person* nn = cur->next;
	free(cur);

	return nn;
}