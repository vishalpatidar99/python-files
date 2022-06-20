# Python program to print all negative numbers in a range
start = int(input("Enter start point "))
end=int(input("Enter end point "))
res=[i for i in range(start,end) if i<0]
print(res)