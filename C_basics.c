#include <stdio.h>

int main(){
    int n, day;

    printf("Enter a number: ");
    scanf("%d", &n);

    if(n > 0){
        printf("Positive number");
    }

    printf("For Loop: ");
    for(int i = 1; i <=5; i++){
        printf("%d", i);
    }

    printf("While Loop");
    int w = 1;
    while(w <= 5){
        printf("%d", w);
        w++;
    }
}