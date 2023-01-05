#include <stdio.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	int i;

	for (i = 1; i <= N; i++)
	{
		for (int j = 0; j < i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}