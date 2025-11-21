public class StringOps {
    public static void main(String[] args){
        String s = "hello";
        System.out.println(s.toUpperCase());
        System.out.println("Reverse = " + new StringBuilder(s).reverse());
    }
    
}
