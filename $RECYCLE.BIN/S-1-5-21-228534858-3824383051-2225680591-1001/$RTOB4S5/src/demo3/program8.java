package demo3;

public class program8 {

	public static void main(String[] args) {
		System.out.println("A main");
		// TODO Auto-generated method stub
	}
}
class B{
	public static void main(String[]args) {
		System.out.println("B main");
		program8.main(new String[0]);
	}

}
