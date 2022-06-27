s= "Ram     goes to  the    school   Ram     daily."
res=""
s=s.split(" ")
# print(s)
for i in s:
    if i != '':
        res+=i+" "
print(res)