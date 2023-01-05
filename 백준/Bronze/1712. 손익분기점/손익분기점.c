#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int ar;
	int as;
	int s;
	int dif = 0;

	scanf("%d %d %d", &ar, &as, &s);
	
	long long int i = 1;

	dif = s - as;

	if (dif <= 0)
	{
		printf("-1");
	}
	else if (dif > 0)
	{
		if (ar % dif == 0)
		{
			printf("%d", ar / dif+1);
		}
		else
			printf("%d", (ar / dif)+1);

	}
	

	return 0;
}