s="cbbcbca"
s.lower()
l=len(s)
t="abc"
res,b,k="","",0
for i in range(l+2):
    if abs(ord(s[0])-ord(s[1]))>0:
        s1=s[2:]
        a=t.replace(s[0],"")
        a=a.replace(s[1],"")
        s=a+s1
        for j in range(k):
            s=c+s[0:]
            l+=1
            k-=1
        if len(s)==1:
            break
    else:
        s1=s[1:]
        c=s[0]
        s=s1
        k+=1
        if len(s)==1:
            for j in range(k):
                s=c+s[0:]
            break
print(s)
print("Done")