# How to count unique values inside a list
ip = [1,2,2,5,8,4,4,8]
res=[]
for i in ip:
    if i not in res:
        res.append(i)
print(len(res))