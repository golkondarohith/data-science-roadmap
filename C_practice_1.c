#include <stdio.h>
int main(){
    //Excersice 1
    int a, b, c;
    printf("The the three numbers: ");
    scanf("%d, %d, %d", &a, &b, &c);
    int sum = a + b + c;
    float avg = sum/3.0;
    printf("The sum is %d\n", sum); 
    printf("The avg is %f", avg);

    //Excersice 3
    int num;
    printf("\nEnter the number: \n");
    scanf("%d", &num);
    if(num > 0){
        printf("The number %d is positve ", num);
    }else if(num < 0){
        printf("The number %d is negative", num);
    }else{
        printf("The number %d is Zero", num);
    }
    return 0;

    //TASK 2
    int num1, num2, num3;
    printf("Enter the 3 numbers: \n");
    scanf("%d %d %d", &num1, &num2, &num3);

    if(num1 > num2){
        if(num1 > num3){
            printf("%d is the Largest number\n", num1);
        }
    }else if(num2 > num1){
        if(num2 > num3){
            printf("%d is the Largest number\n", num2);
        }
    }
    else{
        printf("%d is the Largest number\n", num3);
    }


    //TASK 1
    int a, b;
    printf("Enter a, b values\n");
    scanf("%d%d", &a, &b);

    a = a + b;
    b = a - b;
    a = a -b ;

    printf("%d is new a and %d is new b", a, b);
}