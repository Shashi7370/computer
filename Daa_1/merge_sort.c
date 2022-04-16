#include<stdio.h>
#include<stdlib.h>

void mergesort (int A[], int p, int r){
    int q;
    if (p<r){
        q = (p+r)/2;
        mergesort (A,p,q);
        mergesort (A,q+1,r);
        merge (A,p,r);
    }     
}
int merge (int A[], int p, int q, int r){
    //int n1, n2;
    int n;
    int L[n], R[n], i, j, k;
    int n1 = q-p+1;
    int n2 = r-q;
    n1 = q-p+1;
    n2 = r-q;
    for(i = 1; i<=n1; i++){
        L[i] = A[p+i-1];
    }
    for(j = 1; j<=n2; j++){
        R[j] = A[q+j];
    }
    L[n1+1]=999;
    R[n2+1]=999;
    i=1;
    j=1;
    for(k=p; k<=r; k++){
        if (L[i]<=R[j]){
            A[k]=L[i];
            i++;
        }
        else 
         A[k]=R[i];
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