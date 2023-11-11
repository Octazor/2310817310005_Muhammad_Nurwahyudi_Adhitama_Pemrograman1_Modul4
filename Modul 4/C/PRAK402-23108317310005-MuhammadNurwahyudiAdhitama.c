#include <stdio.h>

int main() {
    int batas, i;

    scanf("%d", &batas);

    if (batas % 2 != 0) {
        batas--;
    }

    for (i = 1; i <= batas; i += 2) {
        printf("%d ", i);
    }

    printf("\n");

    for (i = batas; i >= 2; i -= 2) {
        printf("%d ", i);
    }

    return 0;
}
