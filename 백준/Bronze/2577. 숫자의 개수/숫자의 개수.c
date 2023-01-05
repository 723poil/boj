#include <stdio.h>
#include <math.h>

int main(void)
{
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);

	int mul = 0;
	mul = A * B * C;

	int a[10] = { 0 };
	int p = 0;
	int c = -1;

	for (int i = 0; i < 10; i++)
	{
		p = mul / (int)pow((double)10, (double)i);
		c++;

		if (p == 0)
		{
			break;
		}
	}

	int *b = (int *)malloc(sizeof(int) * (c));

	for (int i = 0; i < c; i++)
	{
		b[i] = (mul / (int)pow((double)10, (double)i)) % 10;
	}

	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (b[j] == i)
			{
				a[i]++;
			}
		}
	}

	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", a[i]);
	}

	return 0;
}