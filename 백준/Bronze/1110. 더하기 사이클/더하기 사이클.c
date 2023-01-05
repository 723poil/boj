#include <stdio.h>

int main(void)
{
	int A;

	scanf("%d", &A);

	int x, y, circle = 0;
	int sum = 0;

	if (A < 10)
	{
		x = 0;
		y = A;
	}
	else
	{
		x = A / 10;
		y = A % 10;
	}

	while (1)
	{
		sum = x + y;
		if (sum >= 10)
		{
			sum = sum % 10;
		}
		x = y;
		y = sum;

		circle++;
		if ((x * 10 + y) == A)
		{
			break;
		}
	}
	printf("%d\n", circle);

	return 0;
}