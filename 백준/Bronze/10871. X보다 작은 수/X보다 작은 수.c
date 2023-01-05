#include <stdio.h>

int main(void)
{
	int N, X;
	scanf("%d %d", &N, &X);

	int i, A;
	for (i = 1; i <= N; i++)
	{
		scanf("%d", &A);
		if (A < X)
		{
			printf("%d ", A);
		}
	}
	return 0;
}