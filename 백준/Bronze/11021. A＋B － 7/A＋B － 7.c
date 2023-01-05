#include <stdio.h>

int main(void)
{
	int T;
	int A, B;

	scanf("%d", &T);

	int x;
	for (x = 1; x <= T; x++)
	{
		scanf("%d %d", &A, &B);
		printf("Case #%d: %d\n", x, A + B);
	}
	return 0;
}