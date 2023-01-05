#include <stdio.h>

int main(void)
{
	int A[9];
	int i;

	for (i = 0; i < 9; i++)
	{
		scanf("%d", &A[i]);
	}
	int max = 0;
	int count = 0;

	for (i = 0; i < 9; i++)
	{
		if (A[i] > max)
		{
			max = A[i];
			count = i+1;
		}
	}
	printf("%d\n%d\n", max, count);

	return 0;
}