# s="abbbcccdaa"
# output a1b3c3d1a2

s="abbbcccdaa"
res=''
count=0

for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count+=1
    if i==(len(s)-1):
        res+=s[i]
        count+=1
        res+=str(count)
    if s[i-1]!=s[i]:
        res+=s[i-1]
        count+=1
        res+=str(count)
        count=0
print(res)
