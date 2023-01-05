#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[1000001];
	gets(str);

	char* delimiter = " ";
	char* pword = strtok(str, delimiter);
	int count = 0;

	while (pword != NULL)
	{
		count++;
		pword = strtok(NULL, delimiter);
	}

	printf("%d\n", count);

	return 0;
}