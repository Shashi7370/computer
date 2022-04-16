#include<stdio.h>

int main(){
    int x=2, y=3, z=3, k=1;
    int result = 3*x/y-z+k;
    // 3*2/3-3+1
    // 6/3-3+1
    // 2-3+1
    // -1+1
    // 0 ans
    printf("The value of this result is %d", result);
    return 0;
}