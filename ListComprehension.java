package encontro12;
import java.util.ArrayList;
public class ListComprehension <P, R> {
	//@Author (name = "Samuel Lincoln Magalhaes Barrocas")
	//Abaixo, Expression eh uma interface funcional em Java, pois ela possui apenas uma declaracao de metodo
	interface Expression <P, R> {
		public R apply (P x);
	}
	//Abaixo, Condition tambem eh uma interface funcional em Java...
	interface Condition <P> {
		public boolean apply (P x);
	}
	public static <P, R> ArrayList <R> make (Expression <P, R> exp, Condition <P> c, ArrayList <P> list) {
		ArrayList <R> ret = new ArrayList <R> ();
		list.forEach (e -> {if (c.apply(e)) {ret.add (exp.apply (e));}});
		return ret;
	}
	public static void main (String [] args) {
		final Integer MAX = 10;
		ArrayList <Integer> l = new ArrayList <Integer> ();
		for (int i = 0; i < MAX; i++) {
			l.add (i);
		}
		ArrayList <String> ls2 = ListComprehension.make (e -> e + " is a number!!", e -> e % 2 == 0, l);
		//A list comprehension acima eh equivalente à seguinte em Python:
			//[e + " is a number!!" for e in l if e % 2 == 0]
		System.out.println (ls2);
	}
}
