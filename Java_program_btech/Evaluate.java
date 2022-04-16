//Q6. Write the program that will read the value of x and evaluate the following function  

import java.util.Scanner;
public class Evaluate
{
    public static void main(String args[]) 
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter x: ");
        int x = in.nextInt();
        int y = -1;
        if (x > 0)
            y = 1;
        else if (x == 0)
            y = 0;
        else
            y = -1;
            
        System.out.println("y=" + y);
    }
}