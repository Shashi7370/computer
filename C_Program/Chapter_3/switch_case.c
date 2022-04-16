#include<stdio.h>

int main(){
    int ratting;
    printf("Enter your ratting (1-5)\n");
    scanf("%d", &ratting);
    switch (ratting)
    {
        case 1:
            printf("Your ratting is 1\n");
            break;
        case 2:
            printf("Your ratting is 2\n");
            break;
        case 3:
            printf("Your ratting is 3\n");
            break;
        case 4:
            printf("Your ratting is 4\n");
            break;
        case 5:
            printf("Your ratting is 5\n");
            break;
       
        default:
            printf("Invalid ratting\n");
            break;
    }
    return 0;
}