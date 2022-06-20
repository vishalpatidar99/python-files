# Ways to remove i’th character from string in Python
str=input("Enter string here: ")
pos=int(input("enter position"))

s=''
for i in range(len(str)):
    if i!=pos-1:
        s=s+str[i]

print(s)