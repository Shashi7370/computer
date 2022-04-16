/* Q19 :- WAP IN JAVA TO DEMONSTRATE THE ROLE OF SUPER KEYWORD.*/
class A
{
	int a=10;
}
class B extends A
{
	int a=20;
	void show()
	{
		System.out.println(a);
		System.out.println(super.a);
	}

}
class Test
{
	public static void main(String[] args)
	{
		B r=new B();
		r.show();
	}
}
