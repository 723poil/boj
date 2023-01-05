#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int Money;
	scanf("%d", &Money);

	printf("%d ", (int)((double)Money * 0.78));

	printf("%d", (int)((double)Money - ((double)Money * 0.2) * 0.22));

	return 0; 
}