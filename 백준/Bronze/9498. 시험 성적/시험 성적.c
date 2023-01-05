#include <stdio.h>

int main(void)
{
	int A, B;

	scanf("%d", &A);

	if (A >= 90 && A <= 100)
	{
		printf("%c\n", 'A');
	}
	else if (A >= 80 && A <= 89)
	{
		printf("%c\n", 'B');
	}
	else if (A >= 70 && A <= 79)
	{
		printf("%c\n", 'C');
	}
	else if (A >= 60 && A <= 69)
	{
		printf("%c\n", 'D');
	}
	else
	{
		printf("%c\n", 'F');
	}

	return 0;
}