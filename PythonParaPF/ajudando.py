glob = []
"""
for i in range (5) :
    for j in range (6) :
        x = j
        y = (lambda x : 2 * x) (x)
        glob.append (y)

print (glob)
"""
#f = lambda : [[(lambda x : 2 * x) (j) for j in range (6)] for i in range (5)]
f = lambda : [[glob.append ((lambda x : 2 * x) (j)) for j in range (6)] for i in range (5)]
f ()
print (glob)
