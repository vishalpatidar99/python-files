from collections import Counter
str=input("Enter string ")
res=Counter(str)
res=max(res, key=res.get)
print(res)