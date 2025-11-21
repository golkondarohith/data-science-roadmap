import java.util.*;
public class Basics {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        //Conditional statements
        System.out.println("Enter a number:");
        int n = sc.nextInt();

        if(n > 0){
            System.out.println("Positive number");

        }

        if(n % 2 == 0){
            System.out.println("Even number");
        }else{
            System.out.println("Odd number");
        }


        //LOOPS
        System.out.println("\n\nFor LOOp");
        for(int i = 1; i <= 5; i++){
            System.out.println(i + " ");
        }

        System.out.println("While LOOP");
        int i = 1;
        while(i <= 5){
            System.out.println(i + " ");
            i++;
        }
    }
}
