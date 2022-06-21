s="ABCDCDCCDC"
sb="CDC"
res=""
c=0
for i in range(0,len(s)):
    if s[i:].startswith(sb):
        c+=1
print(c)