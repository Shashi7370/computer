#include<stdio.h>
#include <cstdlib>
int main ()
{
    int *a,*b;
    a = (int*)malloc(sizeof(int));
    b = (int*)malloc(sizeof(int));
    printf("Enter the value of a\n");
    scanf("%d",a);
    printf("Enter the value of b\n");
    scanf("%d",b);
    printf("The sum of a and b is %d",*a+*b);
    return 0;
}
