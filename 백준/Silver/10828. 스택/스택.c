#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
	int data;
	struct Node* next;
} Node;

typedef struct Stack {
	Node* top;
	int count;
} Stack;

void push(Stack* stack, int data);
int pop(Stack* stack);
int size(Stack* stack);
int empty(Stack* stack);
int top(Stack* stack);

int main(void) {

	int N;
	scanf("%d", &N);

	Stack stack;
	stack.top = NULL;
	stack.count = 0;

	char input[10];

	int i = 0;
	while(i < N) {
		
		scanf("%s", input);
		getchar();

		if (!strcmp(input, "push")) {
			int A;
			scanf("%d", &A);
			push(&stack, A);
		}
		else if (!strcmp(input, "top")) {
			printf("%d\n", top(&stack));
		}
		else if (!strcmp(input, "pop")) {
			printf("%d\n", pop(&stack));
		}
		else if (!strcmp(input, "size")) {
			printf("%d\n", size(&stack));
		}
		else if (!strcmp(input, "empty")) {
			printf("%d\n", empty(&stack));
		}
		else {
			i--;
		}
		i++;
	}

	return 0;
}

void push(Stack *stack, int data) {
	Node* node = (Node*)malloc(sizeof(Node));
	node->data = data;
	node->next = stack->top;
	stack->top = node;
	stack->count++;
}

int pop(Stack* stack) {
	if (stack->top == NULL) {
		return -1;
	}

	Node* node = stack->top;
	int data = node->data;
	stack->top = node->next;
	stack->count--;
	free(node);
	
	return data;
}

int size(Stack* stack) {
	return stack->count;
}

int empty(Stack* stack) {
	if (stack->top == NULL) {
		return 1;
	}
	else {
		return 0;
	}
}

int top(Stack* stack) {
	if (stack->top == NULL) {
		return -1;
	}
	else {
		return stack->top->data;
	}
}