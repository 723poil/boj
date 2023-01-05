#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int data;
	struct Node* next;
} Node;

Node* top;
char sequencearr[200000];
int count = -1;
int overcount = 0;

void push(int data);
void pop();
void possible(int* sequence, int data);

int main(void) {

	top = (Node*)malloc(sizeof(Node));
	top = NULL;

	int n;
	scanf("%d", &n);
	
	int sequence = 1;
	for (int i = 0; i < n; i++) {
		int data;
		scanf("%d", &data);
		possible(&sequence,data);
		if (overcount == -1) {
			break;
		}
	}

	if (overcount == -1) {
		printf("NO");
	}
	else {
		for (int i = 0; i <= count; i++) {
			printf("%c\n", sequencearr[i]);
		}
	}
	return 0;
}

void push(int data) {
	Node* node = (Node*)malloc(sizeof(Node));
	node->data = data;
	node->next = top;
	top = node;
}

void pop() {
	if (top == NULL) {
		return;
	}
	Node* cur = top;
	top = cur->next;
	free(cur);
}

void possible(int* sequence, int data) {
	int True = 1;
	while (True) {
		if (*(sequence) != 1 && top != NULL) {
			if (data == top->data) {
				pop();
				sequencearr[++count] = '-';
				True = 0;
				break;
			}
		}
		if (*(sequence) == data && *sequence != 1) {
			push((*sequence));
			sequencearr[++count] = '+';
			pop();
			sequencearr[++count] = '-';
			True = 0;
			(*sequence)++;
			break;
		}
		push((*sequence));
		sequencearr[++count] = '+';
		if (top->data == data && *sequence != 1) {
			pop();
			sequencearr[++count] = '-';
			True = 0;
			(*sequence)++;
			break;
		}
		if (*sequence > data && top->data > data) {
			overcount = -1;
			return;
		}
		(*sequence)++;
	}
}