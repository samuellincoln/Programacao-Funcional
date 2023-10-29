#modelagem de um grafo
transition = lambda source, arc, dest : (source, arc, dest)
def graph (transition, lst_ts) :
    if (len (transition) != 3) :
        return lst_ts
    else :
        return lambda future_transition : graph (future_transition, lst_ts + [transition])

graph_simp = lambda transition : graph (transition, [])

print_transition_3p = lambda s, a, d : print ("( " + s + " , " + str (a) + " , " + d + " )")
print_transition = lambda tpl : print_transition_3p (tpl [0], tpl [1], tpl [2]) if len (tpl) == 3 else print ("")

p_t = print_transition

print_graph = lambda lst_transitions : [ p_t (lst_transitions [i]) for i in range (len (lst_transitions)) ]

t = transition
t1 = t ("n1", 5, "n2")
t2 = t ("n2", 2, "n3")
t3 = t ("n1", 9, "n3")

g_s = graph_simp

lst_transitions = g_s (t1)(t2)(t3)([])

print_graph (lst_transitions)
