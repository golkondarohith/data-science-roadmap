public class ArrayDemo {
    public static void main(String[] args){
        int[] arr = {5, 1, 4, 2, 3};
        // for(int i = 0; i < arr.length; i++){
        //     System.out.println(arr[i]);
        // }
        for(int x: arr) System.out.print(x + " ");
    }
}
