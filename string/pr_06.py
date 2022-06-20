# Python – Words Frequency in String Shorthands
str=input("Enter string: ")
print(str)

res = {key: str.count(key) for key in str.split()}
print(res)