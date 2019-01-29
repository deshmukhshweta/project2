package example2;

public class program5 {
	static void m1() {
		System.out.println("A main");
	}
	}
class B{
	static void m2() {
		System.out.println("B m2");
	}

	public static void main(String[] args) {
		System.out.println("B main");
		m2();
		program5.m1();
		// TODO Auto-generated method stub

	}

}
