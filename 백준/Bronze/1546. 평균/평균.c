#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	double* a = (double *)malloc(sizeof(double) * (N+1));

	for (int i = 0;i < N;i++)
	{
		scanf("%lf", &a[i]);
	}
	double M = 0;
	for (int i = 0; i < N; i++)
	{
		if (a[i] > M)
		{
			M = a[i];
		}
	}
	double sum = 0;
	for (int i = 0; i < N; i++)
	{
		a[i] = (a[i] / M) * 100;
		sum += a[i];
	}
	printf("%lf\n", sum / (double)N);

	return 0;
}