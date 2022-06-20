# Python | Program to print duplicates from a list of integers
lst=[10,87,34,10,43,23,20,23,20,10]
s=set()
res=set()
for i in lst:
    if i not in s:
        s.add(i)
    else:
        res.add(i)
print(list(res))