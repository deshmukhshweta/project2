package demo2;

public class program7 {
	static void m1(){
		System.out.println("A m1");
	}
}
	class B{
		static void m2(){
			System.out.println("B m2");
		}
	
	public static void main(String[] args) {
		System.out.println(" Bmain");
		m2();
		program7.m1();
	
		// TODO Auto-generated method stub

	}

}
