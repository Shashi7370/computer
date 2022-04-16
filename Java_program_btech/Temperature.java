// Q2.WAP in java to convert the temperature from Fahrenheit to degree Celsius?
import java.util.Scanner;
public class Temperature 
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("\nPlease input Fahrenheight degree: ");
        double fahrenheit=input.nextDouble();
        double celsius=((5*(fahrenheit-32.0))/9.0);
        System.out.println(fahrenheit+ " Fahrenheight degree is equal to " +celsius+ " in Celsius ");
    }
}