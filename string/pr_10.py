def check(string):
    string=string.lower()
    vowels=[string.count('a'),string.count('e'),string.count('e'),string.count('o'),string.count('u')]

    if vowels.count(0)>0:
        print("Not Accepted")
    else:
        print("Accepted")

str=input("Enter string ")
check(str)