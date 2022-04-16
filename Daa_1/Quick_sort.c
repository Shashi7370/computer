#include<stdio.h>

void quicksort (int A[], int p, int r){
    int q;
    if (p<r){
        q = partition (A,p,r);
        quicksort (A,p,q-1);
        quicksort (A,q+1,r);
    }     
}
int partition (int A[], int p, int r){
    int pivot, i, j, temp;
    pivot = A[r];
    i = p-1;
    for(j = p; j<r; j++){
        if(A[j]<=pivot){
            i++;
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    }
    temp = A[i+1];
    A[i+1] = A[r];
    A[r] = temp;
    return (i+1);
}
void main(){
    int j,n,A[10];
    printf("Enter the size of array : \n");
    scanf("%d",&n);
    printf("Enter the element of array :\n");
    for(j=0;j<n;j++)
    scanf("%d",&A[j]);
    quicksort (A,0,n-1);
    printf("Final sorted array is :\n");
    for(j=0;j<n;j++){
        printf("%d \n",A[j]);
    }
}        