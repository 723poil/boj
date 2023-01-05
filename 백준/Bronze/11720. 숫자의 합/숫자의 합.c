#include <stdio.h>

int main(void)
{
	char ch[100];
	int n;
	scanf("%d", &n);
	getchar();

	int i = 0;
	while (i < n)
	{
		scanf("%c", &ch[i]);
		i++;
	}
	int sum = 0;
	for (i = 0;i < n;i++)
	{
		sum += ch[i] - '0';
	}
	printf("%d\n", sum);

	return 0;
}