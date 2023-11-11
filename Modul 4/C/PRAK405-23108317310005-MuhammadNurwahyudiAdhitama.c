#include <stdio.h>

int main(){
    int x, y, i, j;
    scanf("%d %d",&x, &y);

    int hasil = 0;

    for (i = 1; i <= x; i++)
    {
        int total = 0;
        for (j = i; j >= 1; j--)
        {
            int perkalian_kelipatan = j * y;
            printf("(%d * %d)", j, y);
            total += perkalian_kelipatan;
            if (j > 1)
            {
                printf(" + ");
            }
            
        }
        printf(" = %d\n", total);
        hasil += total; 
    
    }

    printf("%d\n", hasil);

    return 0;
}