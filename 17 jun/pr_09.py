# Sample list: [11, 33, 50]
# Expected Output: 113350
ip=[11, 33, 50]
res=''
for i in ip:
    res+=str(i)
res=int(res)
print(res)
print(type(res))
