#include <stdio.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int i = n;
    int j = m;
    while (i < m && j > n){
        printf("%d %d - ", i, j);
        i++;
        j--;
        if (i == m && j == n){
            printf("%d %d", i, j);
        }
    }
    while (i > m && j < n){
        printf("%d %d - ", i, j);
        i--;
        j++;
        if (i == m && j == n){
            printf("%d %d", i, j);
        }
    }
    return 0;
}