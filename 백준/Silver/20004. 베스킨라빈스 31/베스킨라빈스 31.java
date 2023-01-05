import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int A;
		
		Scanner input = new Scanner(System.in);
		A = input.nextInt();
		
		for(int i=1; i<=A; i++) {
			if ( 30 % (i+1) == 0) {
				System.out.printf("%d%n", i);
			}
		}
		input.close();
	}

}
