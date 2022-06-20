# Python program to find largest number in a list
list=[45,7,23,65,2,98]
max=list[0]
for i in list:
    if max<i:
        max=i

print(max)