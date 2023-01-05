#include <stdio.h>
#include <string.h>

int second(char a);

int main(void)
{
	char str[16];
	gets(str);

	int time = 0;
	int i;
	for (i = 0; str[i] != NULL; i++)
	{
		time += second(str[i]);
	}
	printf("%d\n", time);

	return 0;
}

int second(char a)
{
	switch (a)
	{
		case 'A': case 'B': case 'C':
			return 3;
		case 'D': case 'E': case 'F':
			return 4;
		case 'G': case 'H': case 'I':
			return 5;
		case 'J': case 'K': case 'L':
			return 6;
		case 'M': case 'N': case 'O':
			return 7;
		case 'P': case 'Q': case 'R': case 'S':
			return 8;
		case 'T': case 'U': case 'V':
			return 9;
		case 'W': case 'X': case 'Y': case 'Z':
			return 10;
	}
}