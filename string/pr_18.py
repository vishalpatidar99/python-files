# Ways to remove i’th character from string in Python
str=input("Enter string ")
i=int(input("Enter index "))

a=str[:i]
b=str[i+1:]
str=a+b
print(str)