g = lambda l, vertex, edge : [l[i][2] for i in range (len(l)) if l[i][0]==vertex and l[i][1]==edge]
graph = lambda lst_transitions : (lambda vertex : (lambda edge : g (lst_transitions, vertex, edge)))
lst_transitions = [["a", "5", "b"], ["a", "6", "c"], ["b", "1", "c"]]
ga6 = graph (lst_transitions)("a")("6")
gb1 = graph (lst_transitions)("b")("1")
ga5 = graph (lst_transitions)("a")("5")
print (ga6)
print (gb1)
print (ga5)
