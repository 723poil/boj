#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int integer;
	struct Deque* next;
	struct Deque* prev;
} Deque;

int count = 0;

Deque* front;
Deque* back;

void push_front(int data);
void push_back(int data);
int pop_front();
int pop_back();
int size();
int empty();
int Front();
int Back();

int main(void) {

	front = (Deque*)malloc(sizeof(Deque));
	back = (Deque*)malloc(sizeof(Deque));

	front = NULL;
	back = NULL;

	int N;
	scanf("%d", &N);

	int i = 0;
	while (i < N) {
		char input[15];
		scanf("%s", input);

		if (!strcmp(input, "push_back")) {
			int data;
			scanf("%d", &data);

			push_back(data);
		}
		else if (!strcmp(input, "push_front")) {
			int data;
			scanf("%d", &data);

			push_front(data);
		}
		else if (!strcmp(input, "pop_back")) {
			printf("%d\n", pop_back());
		}
		else if (!strcmp(input, "pop_front")) {
			printf("%d\n", pop_front());
		}
		else if (!strcmp(input, "size")) {
			printf("%d\n", size());
		}
		else if (!strcmp(input, "empty")) {
			printf("%d\n", empty());
		}
		else if (!strcmp(input, "front")) {
			printf("%d\n", Front());
		}
		else if (!strcmp(input, "back")) {
			printf("%d\n", Back());
		}
		else {
			printf("input error\n try again\n");
			continue;
		}
		i++;
	}

	return 0;
}

void push_front(int data) {
	Deque* node = (Deque*)malloc(sizeof(Deque));
	node->integer = data;
	if (front == NULL) {
		node->next = back;
		node->prev = NULL;
		front = node;
		back = front;
	}
	else {
		node->next = front;
		node->prev = NULL;
		front->prev = node;
		front = node;
	}
	count++;
}

void push_back(int data) {
	Deque* node = (Deque*)malloc(sizeof(Deque));
	node->integer = data;
	node->next = NULL;
	if (back == NULL) {
		node->prev = NULL;
		back = node;
		front = back;
	}
	else {
		node->prev = back;
		back->next = node;
		back = node;
	}
	count++;
}

int pop_front() {
	if (front == NULL) {
		return -1;
	}
	Deque* cur = front;
	int data = cur->integer;
	if (count == 1) {
		front = NULL;
		back = NULL;
	}
	else {
		front = cur->next;
		front->prev = NULL;
	}
	free(cur);

	count--;
	return data;
}

int pop_back() {
	if (front == NULL) {
		return -1;
	}
	Deque* cur = back;
	int data = cur->integer;
	if (count == 1) {
		back = NULL;
		front = NULL;
	}
	else {
		back = cur->prev;
		back->next = NULL;
	}
	free(cur);

	count--;
	return data;
}

int size() {
	return count;
}

int empty() {
	if (count == 0) {
		return 1;
	}
	else {
		return 0;
	}
}
int Front() {
	if (count == 0) {
		return -1;
	}
	return front->integer;
}

int Back() {
	if (count == 0) {
		return -1;
	}
	return back->integer;
}