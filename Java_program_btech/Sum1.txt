// Q5. WAP in java to determine the sum of the following harmonic series for a given value of n:-
//a. sum = 1+ 2+3+ …………………….+ nth   

import java.util.Scanner;
public class Sum1 
{
    public static void main(String[] args) 
    {
        Scanner r = new Scanner(System.in);
        System.out.println("\nEnter the value of n");
        int n = r.nextInt();
        int sum = 0;
        for (int i = 1; i <= n; i++)
            sum = sum + i;
        System.out.println("\nThe sum of series are " + sum);

    }
}