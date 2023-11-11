#include <stdio.h>

int main() {
    int kelipatan, bilangan, batas;
    char simbol;

    scanf("%d", &kelipatan);

    scanf(" %c", &simbol);

 

    for (bilangan = 1; bilangan <= 50; bilangan++) {
        if (bilangan % kelipatan == 0) {
            printf("%c ", simbol);
        } else {
            printf("%d ", bilangan);
        }
    }

    printf("\n");

    return 0;
}
