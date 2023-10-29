g = lambda l, vertex, edge : [l[i][2] for i in range (len(l)) if l[i][0]==vertex and l[i][1]==edge]
graph = lambda lst_transitions : (lambda vertex : (lambda edge : g (lst_transitions, vertex, edge)))
#lst_transitions = [["a", "5", "b"], ["a", "6", "c"], ["b", "1", "c"], ["a", "1", "d"], ["d", "1", "a"]]
nodes = lambda g : list (set ([g[i][j] for i in range (len (g)) for j in [0, 2]]))
edge = lambda g, sn, dn : [g [i][1] for i in range (len (g)) if g[i][0] == sn and g[i][2] == dn][0]
dest_nodes = lambda g, vertex : [g[i][2] for i in range (len(g)) if g[i][0] == vertex]
all_visited = lambda g, visited : all (vi in visited for vi in nodes (g))
condacc = lambda g, vertex, visited: all_visited (g, visited) or len (dest_nodes (g, vertex)) == 0
min_path_call = lambda g, dn, acc, vertex, visited : minimum_path (g, dn, acc + edge (g, vertex, dn), visited + [dn])

def flat_min (lst) :
    lret = []
    for e in lst :
        if str (type (e)) == "<class 'list'>" :
            lret.append (flat_min (e))
        elif str (type (e)) == "<class 'int'>" or str (type (e)) == "<class 'float'>" :
            lret.append(e)
        else :
            print ()
            #Do nothing
    return min (lret)

graph = [["a", 5, "b"], ["a", 6, "c"], ["a", 3, "d"], ["d", 3, "b"], ["b", 1, "c"], ["c", 1, "d"]]

minimum_path = lambda g, vertex, acc, visited: acc if condacc (g, vertex, visited) else flat_min ([min_path_call (g, dn, acc, vertex, visited) for dn in dest_nodes (g, vertex)])

print (minimum_path (graph, "a", 0, []))
