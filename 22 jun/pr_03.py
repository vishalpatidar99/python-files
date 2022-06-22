s1 = "abcs";
s2 = "cxzca"
res=""
for i in s1:
    if i not in s2:
        res+=i
for j in s2:
    if j not in s1:
        res+=j 
print(res)