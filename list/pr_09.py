# Python program to find smallest number in a list
list=[45,7,23,65,2,98]
min=list[0]
for i in list:
    if min>i:
        min=i

print(min)