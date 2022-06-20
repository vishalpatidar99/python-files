# Python program to print even numbers in a list
list=[12,43,23,88,34]
res=[]
for i in list:
    if i%2==0:
        res.append(i)

print(res)