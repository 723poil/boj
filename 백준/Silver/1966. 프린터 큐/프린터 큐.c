#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int printdata;
	int sequence;
	struct Print* next;
} Print;

Print* front;
Print* rear;

void push(int printdata, int sequence);
int pop(int* sequence);
void freeAll();

int main(void) {

	front = (Print*)malloc(sizeof(Print));
	rear = (Print*)malloc(sizeof(Print));
	front = NULL;
	rear = NULL;

	int T;
	scanf("%d", &T);

	int i = 0;
	int importance[100] = { 0 };
	
	while (i < T) {
		
		int N;
		int M;

		scanf("%d %d", &N, &M);
		
 		for (int j = 0; j < N; j++) {
			scanf("%d", &importance[j]);
			push(importance[j], j);
		}
		// 제일 높은 중요도를 먼저 맨앞으로 배치시킨후
		// 내가 원하는 순서의 데이터가 아니면 
		// pop을 해준후 
		// 다시 그다음 중요도 높은 데이터를 맨앞으로 옮긴다!!
		int True = 1;
		
		int count = 1;
		while (True) {
			
			int max = 1;
			int index = -1;

			for (int j = 0; j < N; j++) {
				if (max < importance[j]) {
					max = importance[j];
					index = j;
				}
			}

			if (max != 1) {
				for (int j = 0; j < N;j++) {
					if (max > front->printdata) {
						int s = 0;
						int data = pop(&s);
						push(data, s);
					}
					else {
						break;
					}
				}
				importance[index] = 0;
			}

			

			if (front->sequence == M) {
				True = 0;
				printf("%d\n", count);
			}
			else {
				int s = 0;
				pop(&s);
			}
			count++;
		}
		freeAll();
		i++;
	}

	return 0;
}

void push(int printdata, int sequence) {
	Print* print = (Print*)malloc(sizeof(Print));
	print->printdata = printdata;
	print->sequence = sequence;
	print->next = NULL;
	if (front == NULL) {
		front = print;
	}
	else {
		rear->next = print;
	}
	rear = print;
}

int pop(int* sequence) {
	Print* temp = front;
	front = temp->next;
	int printdata = temp->printdata;
	*sequence = temp->sequence;
	free(temp);
	
	return printdata;
}

void freeAll() {
	Print* cur = front;
	Print* frev = NULL;

	while (cur != NULL) {
		frev = cur;
		cur = cur->next;
		free(frev);
	}
	front = NULL;
	rear = NULL;
}