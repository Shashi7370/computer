//Q22.WAP in java to define user an exception called Nomatchexception that is thrown when a string is not equal to INDIA. Write a program that //uses this exception? 
class Nomatch extends Exception {
    private String str;
    Nomatch(String str1)
    {
        str=str1;
    }
    public String toString() {
        return "NoMatchException --> String is not India and string is " + str;
    }
}
class P31 {
    public static void main(String[] args) {
        String str1 = new String("India");
        String str2 = new String("Pakistan");
        try {
            if (str1.equals("India"))
                System.out.println(" String is : " + str1);
            else
                throw new Nomatch(str1);
            if (str2.equals("India"))
                System.out.println("\n String is : " + str2);
            else
                throw new Nomatch(str2);
        } catch (Nomatch e) {
            System.out.println("\nCaught ...." + e);
        }
    }
}