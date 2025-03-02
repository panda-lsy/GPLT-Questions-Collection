#include <stdio.h>
int main(){
    int N,num,j=0,k=0;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        scanf("%d",&num);
        if (num%2==0){
            k+=1;
        }
        else{
            j+=1;
        }
    }
    printf("%d %d",j,k);
}