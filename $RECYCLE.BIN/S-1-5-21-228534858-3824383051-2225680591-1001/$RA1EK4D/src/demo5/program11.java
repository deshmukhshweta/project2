package demo5;

public class program11 {
}
class B{

	public static void main(String[] args) {
		System.out.println("B main");
	}
}
	class C{
	
		static void m2() {
			System.out.println("C m2");
		}
		public static void main(String[]args) {
			System.out.println("C main");
			m2();
		}
	}
	class D{
		static void m3() {
			System.out.println("D m3");
		}
		static void m4(){
			System.out.println("D m4");
		}
	}
		class E{
			static void m5() {
				System.out.println("E m5");
			}
			public static void main(String[]args) {
				System.out.println("E main");
				m5();
	           D.m4();
	           D.m3();
	           C.m2();
	           B.main(new String[0]);
			}
			}
	
