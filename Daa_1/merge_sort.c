#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

void mergesort (int A[], int p, int r){
    int q;
    if (p<r){
        q = (p+r)/2;
        mergesort (A,p,q);
        mergesort (A,q+1,r);
        merge (A,p,q,r);
    }     
}
void merge (int A[], int p, int q, int r){
    int n1, n2;
    int L[n1], R[n2], i, j, k;
    n1 = q-p+1;
    n2 = r+q;
    for(i=0; i<n1; i++){
        L[i] = A[p+i-1];
    }
    for(j=0; j<n2; j++){
        R[j] = A[q+j];
    }
    L[n1+1]=INT_MAX;
    R[n2+1]=INT_MAX;
    i=1;
    j=1;
    for(k=p; k<=r; k++){
        if (L[i]<=R[j]){
            A[k]=L[i];
            i++;
        }
        else 
            A[k]=R[j];
            j++; 
    }   
}

void main(){
    int j,n,A[10];
    printf("Enter the size of array : \n");
    scanf("%d",&n);
    printf("Enter the element of array :\n");
    for(j=0;j<n;j++)
    scanf("%d",&A[j]);
    mergesort (A,0,n-1);
    printf("Final sorted array is :\n");
    for(j=0;j<n;j++){
        printf("%d \n",A[j]);
    }
} 