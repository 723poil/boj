#include <stdio.h>

int main(void)
{
	char ch[100];
	scanf("%s", ch);

	int i = 0;
	for (int j = 'a';j <= 'z';j++)
	{
		for (i=0;ch[i] !=NULL;i++)
		{
			if (ch[i] == j)
			{
				printf("%d ", i);
				break;
			}
		}
		if (ch[i] == j)
		{
			continue;
		}
		else
		{
			printf("%d ", -1);
		}
	}
	return 0;
}