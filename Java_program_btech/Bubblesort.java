//Q9.WAP in java to store 20 different names within Array of String and sort them in ascending order by using bubble sort technique?
public class Bubblesort 
{
     public static void main(String[] args)
     {
	int n = 20;		
	String names[]= { "Shashikant", "Ajay", "Gourav", "Riya", "Gita", "Abhishek", "Nidhi", "Nilesh", "Muskan", "Kamal", "Asish", "Mohan", "Tanmay", "Aayusi", "Rajesh", "Abhay", "Dhiraj", "Aditya", "Nikhil", "Deepak"};
	String temp;
	for (int i = 0; i < n; i++) 
        	{
	    for (int j = i + 1; j < n; j++) 
           	    {
	          if (names[i].compareTo(names[j]) > 0) 
               	          {
		temp = names[i];
		names[i] = names[j];
		names[j] = temp;
	          }
	     }
	}
	System.out.println("The names in ascending order are: ");
	for (int i = 0; i < n; i++) 
        	{
	    System.out.println(names[i]);
	}
    }
}