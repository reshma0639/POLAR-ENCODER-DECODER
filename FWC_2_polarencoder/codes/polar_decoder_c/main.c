#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<malloc.h>
#include<string.h>
#include"polar.h"

int main() 
{

int N,K,i;
printf("Enter K :");
scanf("%d",&K);
printf("Enter N :");
scanf("%d",&N);
int *m;
m=(int *) malloc(K*sizeof(int));
for(i=0;i<K;i++)
{
	m[i]=1;
}
int *n;
n=(int *)malloc(N*sizeof(int));
n=polar(m,K,N);
int *dec1;
dec1=(int *)malloc(K*sizeof(int));
dec1=dec(n,K,N);
printf("The polar Encoded signal is :");
for(int i=0;i<N;i++)  
{  
printf("%d", n[i]);  
} 
printf("\nThe polar decoded signal is :\n");
for(int i=0;i<K;i++)  
{  
printf("%d", dec1[i]);  
} 
return 0;  
}
