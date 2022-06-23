l=[(1,2),(3,4,6,723),(123456789,),(134,234,34),(100,1)]
l2,res=[],[]
sort_=0
for i in range(len(l)):
    s=""
    print(l[i])
    for j in l[i]:
        s+=str(j)
    t=len(s)
    l2.append((t,i))
l2.sort()
for k,v in l2:
    res.append(l[v])
print(res)