n=int(input("Enter number here "))
a,b=1,0
c=a+b
for i in range(1,n+1):
    print(c, end=" ")
    a=b
    b=c