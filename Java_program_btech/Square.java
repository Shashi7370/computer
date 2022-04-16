// Q1. WAP in java to find the square root of any positive integer keyed by the user?
import java.util.Scanner;
class Square
{
    public static void main(String[] args)
    {
        int x;
        System.out.print("\nEnter any number\n");
        Scanner r=new Scanner(System.in);
        x=r.nextInt();
        double m=Math.sqrt(x);
        System.out.print("\nSquare root of "+x+" is "+m);
    }
}