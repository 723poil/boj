#include <stdio.h>

int d(int n);

int main(void)
{
	int array1[10000];

	int i = 0;

	for (i = 0; i < 10000; i++)
	{
		array1[i] = i + 1;
	}

	for (i = 0; i < 10000; i++)
	{
		array1[i] = d(i + 1);

		if (array1[i] == 1)
		{
			printf("%d\n", i + 1);
		}
	}
	

	return 0;
}

int d(int n)
{
	int i;

	for (i = 1; i < n; i++)
	{
		int sum = 0;
		sum = i + (i / 1000) + ((i%1000) / 100) + ((i%100) / 10) + (i % 10);

		if (sum == n)
		{
			return 0;
		}
	}

	return 1;
}