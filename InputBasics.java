import java.util.*;


public class InputBasics{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println("Sum = " + (a+b));
        System.out.println("Max = " + Math.max(a, b));
    }
}