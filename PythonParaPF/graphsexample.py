#Exemplo de grafo nao direcionado...
dest_node_edge = lambda g, vertex, edge : [g[i][2] for i in range (len(g)) if g[i][0]==vertex and g[i][1]==edge]
traverse = lambda g : (lambda vertex : (lambda edge : dest_node_edge (g, vertex, edge)))

edge = lambda g, sn, dn : [g [i][1] for i in range (len (g)) if g[i][0] == sn and g[i][2] == dn][0]

nodes = lambda g : list (set ([g[i][j] for i in range (len (g)) for j in [0, 2]]))

graph = [["a", 3, "b"], ["a", 11, "c"], ["b", 7, "c"]]

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

dest_nodes = lambda g, vertex : [g[i][2] for i in range (len(g)) if g[i][0]==vertex]
all_visited = lambda g, visited : all (vi in visited for vi in nodes (g))
condacc = lambda g, vertex, visited: all_visited (g, visited) or len (dest_nodes (g, vertex)) == 0
min_path_call = lambda g, dn, acc, vertex, visited : minimum_path (g, dn, acc + edge (g, vertex, dn), visited + [dn])
minimum_path = lambda g, vertex, acc, visited: acc if condacc (g, vertex, visited) else flat_min ([min_path_call (g, dn, acc, vertex, visited) for dn in dest_nodes (g, vertex)])

print (minimum_path (graph, "a", 0, []))
