l=[['a','b',1,2],['c','d',3,4],['e','f',5,6]]
res={}
for i in l:
    k,v=[],[]
    for j in i:
        if type(j)==str:
            k.append(j)
        else:
            v.append(j)
    res.update({tuple(k):tuple(v)})
    
print(res)