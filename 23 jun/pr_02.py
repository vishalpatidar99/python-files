s="cbbcbca"
s.lower()
t="abc"
res=""
i=True

while i:
    t="abc"
    if len(s)==1:
        i=False
        print(s)
        break
    for j in range(len(s)-1):
        # import pdb;pdb.set_trace()
        if s[j]!=s[j+1]:
            if j==0:
                s1=s[j+2:]
                a=t.replace(s[j],"")
                a=a.replace(s[j+1],"")
                s=a+s1
                # print(s)
                # import pdb;pdb.set_trace()
                break
            elif j==len(s)-2:

                s1=s[:j]
                a=t.replace(s[j],"")
                a=a.replace(s[j+1],"")
                s=s1+a
                # print(s)
                break

            else:
                # import pdb;pdb.set_trace()
                s1=s[:j]
                s2 = s[j+2:]
                a=t.replace(s[j],"")
                a=a.replace(s[j+1],"")
                s=s1 +a +s2
                # print(s)
                break
        elif s[j]==s[j+1]:
            if j==len(s)-2:
                print(s)
                i=False
                break
            pass
        else:
            i=False
print("Done")