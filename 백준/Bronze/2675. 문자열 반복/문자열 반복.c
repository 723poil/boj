#include <stdio.h>
#include <string.h>

int main(void)
{
	int testcase;
	int repeat;
	char line[1000][20];

	scanf("%d", &testcase);

	int i = 0;
	while (i < testcase)
	{
		scanf("%d %s", &repeat, line[i]);
		for (int j = 0; line[i][j] != NULL; j++)
		{
			for (int k = 0; k < repeat; k++)
			{
				printf("%c", line[i][j]);
			}
		}
		printf("\n");
		i++;
	}

	return 0;
}