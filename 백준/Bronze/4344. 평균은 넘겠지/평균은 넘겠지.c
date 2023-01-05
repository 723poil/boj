#include <stdio.h>
#include <string.h>

int main(void)
{
	int N;
	scanf("%d", &N);

	double a[1000];
	int c;

	while (N--)
	{
		scanf("%d", &c);
		int i = 0;
		int count = 0;
		while (c--)
		{
			scanf("%lf", &a[i]);
			i++;
		}
		c = i;

		double sum = 0;

		for (i = 0; i<c; i++)
		{
			sum += a[i];
		}
		double avg = sum / (double) c;

		for (i = 0; i<c; i++)
		{
			if (a[i] > avg)
			{
				count++;
			}
		}
		printf("%.3lf%%\n", ((double) count / (double) c) * (double) 100);
	}

	return 0;
}