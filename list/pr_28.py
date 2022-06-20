# Python | Sum of number digits in List
list=[12,54,34,56]
res=[]
for i in list:
    sum=0
    for j in str(i):
        sum+=int(j)
    res.append(sum)

print(res)