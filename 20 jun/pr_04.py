from numpy import product

ip=[1, 3, 5, 6, 3, 5, 6, 1]
res=[]
for i in ip:
    if i not in res:
        res.append(i)

print(product(res))