#include <stdio.h>

int main() {
	int num, i = 1, j, tri[500][500] = { 0 };

	for (scanf("%d", &num); i <= num; i++) for (j = 0; j < i; j++) scanf("%d", &tri[i - 1][j]);

	while (num--) for (i = 0; i < num; i++) tri[num - 1][i] += tri[num][i] > tri[num][i + 1] ? tri[num][i] : tri[num][i + 1];
	printf("%d", tri[0][0]);
}