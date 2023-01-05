#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int data;
	struct Node* next;
} Node;

typedef struct {
	Node* front;
	Node* rear;
	int count;
} Queue;

void push(Queue* queue, int data);
int pop(Queue* queue);
int size(Queue* queue);
int empty(Queue* queue);
int front(Queue* queue);
int back(Queue* queue);

int main(void) {

	Queue queue;
	queue.count = 0;
	queue.front = NULL;
	queue.rear = NULL;

	int N;
	scanf("%d", &N);

	int i = 0;
	char input[10];
	while (i < N) {
		scanf("%s", input);
		getchar();

		if (!strcmp(input, "push")) {
			int num;
			scanf("%d", &num);

			push(&queue, num);
		}
		else if (!strcmp(input, "pop")) {
			printf("%d\n", pop(&queue));
		}
		else if (!strcmp(input, "size")) {
			printf("%d\n", size(&queue));
		}
		else if (!strcmp(input, "empty")) {
			printf("%d\n", empty(&queue));
		}
		else if (!strcmp(input, "front")) {
			printf("%d\n", front(&queue));
		}
		else if (!strcmp(input, "back")) {
			printf("%d\n", back(&queue));
		}
		i++;
	}

	return 0;
}

void push(Queue* queue, int data) {
	Node* node = (Node*)malloc(sizeof(Node));
	node->data = data;
	node->next = NULL;

	if (queue->count == 0) {
		queue->front = node;
	}
	else {
		queue->rear->next = node;
	}
	queue->rear = node;
	queue->count++;
}

int pop(Queue* queue) {
	if (queue->count == 0) {
		return -1;
	}
	Node* node = queue->front;
	int data = node->data;
	queue->front = node->next;
	free(node);
	queue->count--;
	return data;
}

int size(Queue* queue) {
	return queue->count;
}

int empty(Queue* queue) {
	if (queue->count == 0) {
		return 1;
	}
	else {
		return 0;
	}
}

int front(Queue* queue) {
	if (queue->count == 0) {
		return -1;
	}
	else {
		return queue->front->data;
	}
}

int back(Queue* queue) {
	if (queue->count == 0) {
		return -1;
	}
	else {
		return queue->rear->data;
	}
}