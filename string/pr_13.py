from collections import Counter
str=input("Enter string ")
res= Counter(str)
res=min(res, key=res.get)
print(res)