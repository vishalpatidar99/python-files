# Python program to find N largest elements from a list# Python program to find second largest number in a list
list=[23,58,4,56,34,51]
N=int(input("Enter term "))
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list[:N])