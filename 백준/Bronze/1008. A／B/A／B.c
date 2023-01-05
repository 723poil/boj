#include <stdio.h>

int main(void)
{
	int A, B;

	scanf("%d %d", &A, &B);
	printf("%.9lf\n",(double) A / (double) B);

	return 0;
}