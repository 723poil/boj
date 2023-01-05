#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100001

int heap[MAX_SIZE] = { 0 };
int n = 0;

void insertion(int data);
int pop();

int main(void) {
	
	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		int data;
		scanf("%d", &data);

		if (data == 0) printf("%d\n", pop());
		else {
			insertion(data);
		}
	}


	return 0;
}

void insertion(int data) {
	if (!n) {
		heap[++n] = data;
		return;
	}
	int i = ++n;

	while ((i != 1) && (data < heap[i / 2])) {
		heap[i] = heap[i / 2];
		i /= 2;
	}
	heap[i] = data;
}

int pop() {
	if (n == 0) return 0;
	int data = heap[1];

	int temp = heap[n--];
	int parent = 1;
	int child = 2;
	while (child <= n) {
		if ((child < n) && (heap[child] > heap[child + 1])) {
			child++;
		}
		if(temp <= heap[child]) break;
		heap[parent] = heap[child];
		parent = child;
		child *= 2;
	}
	heap[parent] = temp;

	return data;
}