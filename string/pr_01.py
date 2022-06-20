# Python program to check if a string is palindrome or not
str=input("Enter string here: ")
s=str[::-1]
if s==str:
    print("its Palindrome")
else:
    print("its not Palindrome")
