s="GeeksforGeeks"
s.lower()
res=""
for i in s:
    if i not in res:
        res+=i
print(res)
c=0
for j in res:
    if j=="a":
        c+=1
    if j=="e":
        c+=1
    if j=="i":
        c+=1
    if j=="o":
        c+=1
    if j=="u":
        c+=1
print(c)