#include <stdio.h>
#include <string.h>

int toint(char* n);

int main(void)
{
	char su1[4];
	char su2[4];

	scanf("%s", su1);

	scanf("%s", su2);

	if (toint(su1) > toint(su2))
	{
		printf("%d\n", toint(su1));
	}
	else
	{
		printf("%d\n", toint(su2));
	}

	return 0;
}

int toint(char* n)
{
	int a, b, c;

	a = 100 * (*(n + 2) - '0');
	b = 10 * (*(n + 1) - '0');
	c = *(n + 0) - '0';

	return a + b + c;
}