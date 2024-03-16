import java.util.ArrayList;
import java.util.List;

public class TesteFuncional {
	//Todas as interfaces funcionais aqui sao closures
	//Abaixo, Expression eh uma interface funcional em Java, pois ela possui apenas uma declaracao de metodo
	interface Expression <R, P> {
		public R apply (P x);
	}
	//Abaixo, Condition tambem eh uma interface funcional em Java...
	interface Condition <P> {
		public boolean apply (P x);
	}
	//Abaixo, vemos uma classe que implementa List Comprehension,
		//pegando como parametro uma Expression, um ArrayList e uma Condition...
	class ListComprehension <R, E> {
		public ArrayList <R> apply (Expression <R, E> exp, ArrayList <E> param, Condition <E> condition) {
			ArrayList <R> retl = new ArrayList <R> ();
			for (int i = 0; i < param.size(); i++) {
				E e = param.get (i);
				if (condition.apply (e)) {
					retl.add ((R)exp.apply (e));
				}
			}
			return retl;
		}
	}
	//Abaixo, uma pequena interface funcional
	interface F {
		public int apply (int x);
	}
	//Abaixo, a interface funcional HOF representa uma funcao de alta ordem, pois possui
	// uma funcao (variavel do tipo interface funcional F) como parametro de seu metodo unico... 
	interface HOF {
		public int apply (F f, int x);
	}
	//Abaixo, uma funcao que utilizaremos para ilustrar currying
	interface HOF_Currying {
		public F apply (int x);
	}
	public static void main (String [] args) {
		//Abaixo, inicializamos a nossa funcao lambda do tipo interface funcional F
		F f = x -> 3 * x;
		//Nas duas proximas linhas, instanciamos uma funcao do tipo interface funcional HOF_Currying,
		//	e aplicamos currying na linha seguinte
		HOF_Currying hofc = (x) -> (z -> 3 * (x + z));
		int ret = ((F)hofc.apply (3)).apply(0);
		System.out.println ("Apos o currying hofc (3)(0), eh retornado " + ret);
		//Abaixo, instanciamos uma funcao do tipo interface funcional HOF
		HOF hof = (func, x) -> {return func.apply(x);};
		System.out.println (hof.apply (f, 5));

		//Abaixo, criamos a nossa ListComprehension que ira pegar a lista alparam como parametro e ira
		// filtrar os elementos de modo que apenas os elementos pares serao incluidos...
		ListComprehension <Integer, Integer> lc = (new TesteFuncional ()).new ListComprehension <Integer, Integer> ();

		ArrayList <Integer> alparam = new ArrayList <Integer> ();

		//alparam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		List <Integer> alparamaux = List.of (0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
		alparamaux.forEach (e -> alparam.add (e));

		//al = [e for e in l if e % 2 == 0]
		ArrayList <Integer> al = (ArrayList<Integer>) lc.apply (e -> e, alparam, x -> x % 2 == 0);

		System.out.println ("Elementos da lista al abaixo:");

		al.forEach(e -> System.out.print (e + ", "));

		System.out.println ("Elementos da lista al acima");

		//A instrucao abaixo eh equivalente a F f_2 = x -> 3 * x
		F f_2 = new F () {public int apply (int x) {return 3 * x;}};
		System.out.println (f.apply (5));
	}
}
