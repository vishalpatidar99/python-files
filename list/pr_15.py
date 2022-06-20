# Python program to print all even numbers in a range
start=int(input("Enter start point "))
end=int(input("Enter end point "))
for i in range(start,end+1):
    if i%2==0:
        print(i, end=" ")