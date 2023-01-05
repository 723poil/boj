#include <stdio.h>

int d(int n);

int main(void)
{
	int N;
	scanf("%d", &N);
	printf("%d\n", d(N));

	return 0;
}

int d(int n)
{
	int i;
	int count = 0;

	for (i = 1; i <= n; i++)
	{
		if (i < 100)
		{
			count++;
		}
		else if (i >= 100)
		{
			int dif1;
			int dif2;

			dif1 = i / 100 - (i % 100) / 10;
			dif2 = (i % 100) / 10 - i % 10;

			if (dif1 == dif2)
			{
				count++;
			}
		}
	}
	return count;
}