/* Q25 :- WAP IN JAVA TO DEMONSTRATE THE ROLE OF synchronized KEYWORD.*/
class Syn
{
     public synchronized void printSyn(int n)
     {
        for(int i=1;i<=10;i++)
        {
            System.out.println(n*i);
         }
     }
}
class thread1 extends Thread
{
	 Syn t;
   	 thread1(Syn t)
	{
        	     this.t=t;
    	}
	public void run()
    {
        t.printSyn(4);
    }
}
class thread2 extends Thread
{
	Syn t;
  	thread2(Syn t)
	{
        	      this.t=t;
    	}
	public void run()
    {
        t.printSyn(9);
    }
}
class Main
{
	public static void main(String[] args)
	{
		Syn obj=new Syn();

       		 thread1 t1=new thread1(obj);
        		 thread2 t2=new thread2(obj);

       		 t1.start(); t2.start();
	}
}