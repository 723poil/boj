#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	int *A = (int *)malloc(sizeof(int) * (N+1));
	int i;
	int max = -1000000, min = 1000000  ;

	for (i = 0; i < N; i++)
	{
		scanf("%d", &A[i]);
	}

	for (i = 0; i < N; i++)
	{
		if (A[i] > max)
		{
			max = A[i];
		}
		if (A[i] < min)
		{
			min = A[i];
		}
	}

	printf("%d %d\n", min, max);

	return 0;
}