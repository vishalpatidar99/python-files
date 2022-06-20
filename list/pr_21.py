# Remove multiple elements from a list in Python
list=[12,54,54,43,56,43]
num1,num2=int(input("Enter number ")),int(input("Enter number "))
for i in list:
    if num1==i or num2==i:
        list.remove(i)
print(list)