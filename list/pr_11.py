# Python program to find second largest number in a list
list=[23,58,4,56,34,51]
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list[1])