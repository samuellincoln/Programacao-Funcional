package encontro12;

import java.util.ArrayList;

public class UsingLC {
	public static void main (String [] args) {
		ArrayList <Integer> l = new ArrayList <Integer> ();
		for (int i = 0; i < 10; i++) {
			l.add (i);
		}
		ArrayList <String> ls2 = ListComprehension.make (e -> e + " is a number!!", e -> e % 2 == 0, l);
		System.out.println (ls2);
	}
}