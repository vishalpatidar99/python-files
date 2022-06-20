# Reverse words in a given String in Python
str=input("Enter string here: ")
s=str.split()[::-1]
l=[]

for i in s:
    l.append(i)

print(' '.join(l))