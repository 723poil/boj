#include <stdio.h>

int main(void)
{
	char ch[1000001];
	int count[26] = { 0, };

	scanf("%s", ch);

	for (int i = 0; ch[i] != NULL;i++)
	{
		if (90 >= ch[i] && ch >= 65)
		{
			count[ch[i] - 65]++;
		}
		else if (122 >= ch[i] && ch[i] >= 97)
		{
			count[ch[i] - 97]++;
		}
	}

	int maxx;
	int max = 0;

	for(int i = 0;i < 26; i++)
	{
		if (count[i] > max)
		{
			max = count[i];
			maxx = i;
		}
	}
	

	for (int i = 0; i <26; i++)
	{
		if (maxx == i)
		{
			continue;
		}
		else if (max == count[i])
		{
			maxx = '?';
		}
	}
	if (maxx == '?')
		printf("?");
	else
		printf("%c", maxx + 65);

	return 0;
}