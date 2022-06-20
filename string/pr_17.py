str=input("Enter string ")
str=str.split()
print(str)
k=3
string=[]

for x in str:
    if len(x)>k:
        string.append(x)

print(string)
