dados_funcionarios = {"Manoel Ribeiro" : ["045", 5000], "Pedro Silva" : ["547", 5000], "Samuel Lima" : ["123", 5000]}
#lsts_with_new_field = list (lambda e : map (lambda ls : ls + [e], [dados_funcionarios [k] for k in dados_funcionarios.keys()]))

#def updated_dic (dic, lsts):
#    retdic = {}
#    keys = list (dic.keys())
#    for i in range (len (keys)) :
#        retdic.update({keys [i] : lsts [i]})
#    return retdic

#print (updated_dic (dados_funcionarios, lsts_with_new_field ("Analista de TI")))

def flat_map (f, lst) :
    lret = []
    for e in lst :
        if str (type (e)) == "<class 'list'>" :
            lret += flat_map (f, e)
        elif str (type (e)) == "<class 'int'>" :
            lret.append(f (e))
        else :
            print ()
            #Do nothing
    return lret

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

print (flat_min ([2, 3, 4, 5, [4, 5.5, 6, [1, 56, 110]]]))
#print (min ([2, 3, 4, 5.5]))
#print (type (5.5))
