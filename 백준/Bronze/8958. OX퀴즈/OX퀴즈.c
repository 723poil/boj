#include <stdio.h>
#include <string.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	char a[79];

	while (N--)
	{
		int sum = 0;
		int count = 0;
		scanf("%s", a);
		for (int i = 0; i < strlen(a); i++)
		{
			if (a[i] == 'O')
			{
				count++;
				sum += count;
			}
			else
			{
				count = 0;
			}
		}
		printf("%d\n", sum);
	}

	return 0;
}