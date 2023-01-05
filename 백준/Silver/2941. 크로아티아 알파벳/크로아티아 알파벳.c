#include <stdio.h>

int main(void)
{
	char str[101];
	gets(str);

	int count = 0;

	for (int i = 0; str[i] != NULL;i++)
	{
		count++;
		if (str[i] == '=')
		{
			count--;
			if (str[i - 2] == 'd' && str[i - 1] == 'z')
			{
				count--;
			}
		}
		else if (str[i] == '-')
		{
			count--;
		}
		else if (str[i] == 'j' && (str[i - 1] == 'l' || str[i - 1] == 'n'))
		{
			count--;
		}
	}

	printf("%d\n", count);

	return 0;
}