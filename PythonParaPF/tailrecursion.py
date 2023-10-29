import sys
left_sublist = lambda pivot, vec : [x for x in vec if x < pivot]
right_sublist = lambda pivot, vec : [x for x in vec if x > pivot]
median = lambda vec : vec [len (vec) // 2]

ls = lambda vec : left_sublist (median (vec), vec)
rs = lambda vec : right_sublist (median (vec), vec)

is_ordered = lambda vec : all ([vec [i] <= vec [i + 1] for i in range (len (vec) - 1)])

quick = lambda vec : vec if is_ordered (vec) else quick (ls (vec) + [median (vec)] + rs (vec))

quicksort = lambda vec : quick (vec)
#print (quicksort ([5, 3, 9, 1, 11]))#, 33, 44, 55, 66, 77, 88, 54, 47, 31]))
#print (quicksort ([22, 16, 88, 44, 33]))
#print (quicksort ([5, 3, 9, 1]))#, 33, 44, 55, 66, 77, 88, 54, 47, 31]))
#print (quicksort ([5, 3, 9]))#, 33, 44, 55, 66, 77, 88, 54, 47, 31]))
#print (quicksort ([5, 3]))#, 33, 44, 55, 66, 77, 88, 54, 47, 31]))
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print (quicksort ([9, 8, 7, 6, 5, 4, 3, 2, 1]))
