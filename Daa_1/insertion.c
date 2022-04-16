#include<stdio.h>

int main(){
    int i,j,n,a[10],key;
    printf("Enter the size of array : \n");
    scanf("%d",&n);
    printf("Enter the element of array :\n");
    for(j=0;j<n;j++)
    scanf("%d",&a[j]);

    for(j=1;j<n;j++){
        i=j-1;
        key=a[j];
        while (i>=0 && a[i]>key)
        {
            a[i+1]=a[i];
            i--;
        }
        a[i+1]=key;
    }
    printf("Final sorted array is :\n");
    for(j=0;j<n;j++){
        printf("%d \n",a[j]);
    }
    return 0;
}
