import time
def not_lazy_range (n) :
    r = []
    i = 0
    while i < n :
        r.append (i)
        i = i + 1
    return r
maxr = 10000000
print ("Processing with Not Lazy range")
for i in range (10) :
    t0 = time.time ()
    l = map (lambda x : 3 * x + 1, not_lazy_range (maxr))
    print(list (l) [7])
    print (time.time () - t0)
print ("Processing with Lazy/Regular range")
for i in range (10) :
    t0 = time.time ()
    l = map (lambda x : 3 * x + 1, range (maxr))
    print(list (l) [7])
    print (time.time () - t0)
