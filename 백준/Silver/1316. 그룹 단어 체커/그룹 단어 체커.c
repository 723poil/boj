#include <stdio.h>
#include <string.h>

int select(char a[], int len);

int main(void)
{
	int N;
	scanf("%d ", &N);

	char str[101];
	int count = N;

	for (int i = 0; i < N;i++)
	{
		scanf("%s", str);
		count -= select(str, strlen(str)+1);
	}
	printf("%d\n", count);

	return 0;
}

int select(char a[], int len)
{
	for (int i = 0; i < len; i++)
	{
		for (int j = 0; j < len; j++)
		{
			if (a[i] == a[j] && j - i > 1)
			{
				if (a[j] != a[j - 1])
				{
					return 1;
				}
			}
		}
	}
	return 0;
}