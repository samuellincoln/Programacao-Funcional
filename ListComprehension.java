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
}
