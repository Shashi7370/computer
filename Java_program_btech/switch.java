import java.io.*;
class Switch
{
   public static void main(String args[ ]) throws IOException
            {
	DataInputStream in=new DataInputStream(System.in);
	System.out.print("\n\n Fee structure of b.tech semester wise \n");
	System.out.print("\n\n 1. 1st semester\n 2. 2nd semester\n 3. 3rd semester\n 4. 4th semester\n 5. 5th semester\n 6. 6th semester\n 7. 7th semester\n 8. 8th semester\n\n\n\n");
	System.out.print("Please enter your choice whose semester's fee you want to know.\n\n");
	int n=Integer.parseInt(in.readLine( ) );
	 switch(n)
	     {
		case 1 :
		  System.out.print("\nFee of 1st semester is 45000\n\n");
		  break;
		case 2 :
		  System.out.print("\nFee of 2nd semester is 37000\n\n");
		  break;
		case 3 :
		  System.out.print("\nFee of 3rd semester is 35250\n\n");
		  break;
		case 4 :
		  System.out.print("\nFee of 4th semester is 37750\n\n");
		  break;
		case 5 :
		  System.out.print("\nFee of 5th semester is 34250\n\n");
		  break;
		case 6 :
		  System.out.print("\nFee of 6th semester is 33750\n\n");
		  break;
		case 7 :
		  System.out.print("\nFee of 7th semester is 34250\n\n");
		  break;
		case 8 :
		  System.out.print("\nFee of  8th semester is 32750\n\n");
		  break;
		default :
		  System.out.print("\nsorry please select given case in the list\n\n\n");
	   }
        }
}
		