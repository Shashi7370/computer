//Q10.WAP in Java to store 20 integers within Array and sort the array in ascending order using bubble sort technique. 
import java.util.Scanner;

public class Bubblesort1 {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int arr[] = new int[20];
        System.out.println("Enter 20 numbers:");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = in.nextInt();
        }
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int t = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = t;
                }
            }
        }
        System.out.println("\nSorted Array are:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}