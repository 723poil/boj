#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int booleanVPS(char vps[]);

int main(void) {

	int N;
	scanf("%d", &N);

	int i = 0;
	while (i < N) {

		char vps[50];
		scanf("%s", vps);
		
		if (booleanVPS(vps) == 0) {
			printf("NO\n");
		}
		else {
			printf("YES\n");
		}

		i++;
	}

	return 0;
}

int booleanVPS(char vps[]) {
	
	int leftcount = 0;

	for (int i = 0; vps[i] != NULL; i++) {
		if (vps[i] == '(') {
			leftcount++;
		}
		else if (vps[i] == ')') {
			leftcount--;
			if (leftcount < 0) {
				return 0;
			}
		}
	}
	if (leftcount != 0) {
		return 0;
	}
	else {
		return 1;
	}
}