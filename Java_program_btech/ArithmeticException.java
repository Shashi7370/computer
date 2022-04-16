//Q23. Write the program in java that handles three types of exception? 
// There are three types of exception
 
// 1----- Java program to demonstrate ArithmeticException
    class ArithmeticException
    {
        public static void main(String args[])
        {
            try {
                int a = 30, b = 0;
                int c = a/b; // cannot divide by zero
                System.out.println ("Result = " + c);
            }
            catch(ArithmeticException e) {
                System.out.println ("Can't divide a number by 0");
            }
        }
    }