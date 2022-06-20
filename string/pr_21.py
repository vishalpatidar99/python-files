A="geeks for geeks"
B="learning from geeks for geeks"
count={}

for x in A.split():
    count[x]=count.get(x,0)+1

for x in B.split():
    count[x]=count.get(x,0)+1

res=[x for x in count if count[x]==1]
print(res)