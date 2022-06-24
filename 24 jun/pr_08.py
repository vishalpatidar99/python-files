# The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
# The character list is : ['g', 'o']
# The filtered strings are : ['is', 'best']
ip=['gfg','is','best','for','geeks']
k=['g','o']
res=[]
for i in ip:
    t=0
    for j in k:
        if j not in i:
            t+=1
        if t==len(k):
            res.append(i)
print(res)