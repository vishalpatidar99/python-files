import re
str=input("Enter string ")
regex=re.compile('[!@#$%^&*()<>?/\|}{~:]')

if regex.search(str)==None:
    print("String Accepted")
else:
    print("String Not Accepted")