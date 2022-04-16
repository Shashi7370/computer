import java.util.Scanner;

//Q7. WAP in java to compute the sum of the digits of any positive number 
public class Digit_sum 
{
    public static void main(String[] args)
    {
        int m, n;
        int sum=0;
        Scanner sr = new Scanner(System.in);
        System.out.print("\nEnter the number\n");
        m=sr.nextInt();

        while (m>0)
        {
            n=m%10;
            sum=sum+n;
            m=m/10;
        }
        System.out.println("\nSum of Digit:=" +sum);
    }
}