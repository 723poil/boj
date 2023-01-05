#include <stdio.h>

int main(void)
{
	int A[10];
	int B = 42;
	int C[10];

	for (int i = 0;i < 10; i++)
	{
		scanf("%d", &A[i]);
	}

	for (int i = 0; i < 10; i++)
	{
		C[i] = A[i] % B;
	}

	int count = 0;
	int count1 = 0;
	int count2 = 0;

	for (int i = 0; i < 10; i++)
	{
		for (int j = i + 1; j < 10; j++)
		{
			if (C[i] != NULL || C[j] != NULL)
			{
				if (C[i] == C[j])
				{
					C[j] = NULL;
					count1++;
				}
			}
		}
	}
	for (int i = 0; i < 10; i++)
	{
		if (C[i] == NULL)
		{
			count2++;
		}
		if (C[i] != NULL)
		{
			count++;
		}
	}
	if (count1 != count2)
	{
		count++;
	}
	printf("%d\n", count);

	return 0;
}