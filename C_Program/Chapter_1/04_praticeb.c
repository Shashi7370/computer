#include<stdio.h>

int main(){
    int principal, rate, years;    
    printf("Enter The value of principal is\n");
    scanf("%d",&principal);
    printf("Enter The value of rate is\n");
    scanf("%d",&rate);
    printf("Enter The value of years is\n");
    scanf("%d",&years);
    printf("The value of SimpleIntrest is %d",(principal*rate*years)/100);
    return 0;
}