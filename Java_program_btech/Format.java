/*Q3. WAP in java to display the following format :-
     a.        1
	1  2
	1  2  3
	1  2  3  4
	1  2  3  4  5
		*/
class Format
{
     public static void main(String[] args)
     {
         for(int i=1;i<=5;i++)
         {
	for(int j=1;j<=i;j++)
	{
	   System.out.print(+j+"\t");
	}
	   System.out.println();
          }
     }
}