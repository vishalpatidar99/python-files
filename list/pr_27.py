# Python program to find Cumulative sum of a list
list=[34,23,13,4,54,76]
j=0
res=[]
for i in list:
    j+=i
    res.append(j)

print(res)