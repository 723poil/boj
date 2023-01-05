#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int money;
	struct moneyStack* next;
} moneyStack;

moneyStack* top;

void push(int money);
void pop();
int sum();

int main(void) {

	int K;
	scanf("%d", &K);



	for (int i = 0; i < K; i++) {
		int integer;
		scanf("%d", &integer);
		if (integer == 0) {
			pop();
		}
		else {
			push(integer);
		}
	}

	printf("%d\n", sum());

	return 0;
}

void push(int money) {
	moneyStack* temp = (moneyStack*)malloc(sizeof(moneyStack));
	temp->money = money;
	temp->next = top;
	top = temp;
}

void pop() {
	if (top == NULL) {
		printf("Stack empty\n");
		return 999999;
	}
	moneyStack* cur = top;
	top = cur->next;
	free(cur);
}

int sum() {
	moneyStack* cur = top;
	int sum = 0;

	while (cur != NULL) {
		sum += cur->money;
		cur = cur->next;
	}

	return sum;
}