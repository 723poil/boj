#include <stdio.h>

int main(void)
{
	int A, B;

	scanf("%d %d", &A, &B);

	if (A > B)
	{
		printf("%c\n", '>');
	}
	else if (A < B)
	{
		printf("%c\n", '<');
	}
	else
	{
		printf("%c%c", '=', '=');
	}

	return 0;
}