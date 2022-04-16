#include<stdio.h>

int main(){
    int length, breadth;
    printf("Enter the length of this rectangle is\n");
    scanf("%d",&length);

    printf("Enter the Breadth of this rectangle is\n");
    scanf("%d",&breadth);
    
    printf("The area of this rectangle is %d",length*breadth);
    return 0;
}