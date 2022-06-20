# Python program to check whether the string is Symmetrical or Palindrome
str=input("Enter string here: ")
half=int(len(str)/2)
first_str=str[:half]
second_str=str[half:]

if first_str==second_str:
    print("its symmetric")
else:
    print("its not symmetric")

if first_str==second_str[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")