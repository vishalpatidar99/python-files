# Python Program to check Armstrong Number
num=int(input("Enter nuber "))
count,sum,temp1,temp2=0,0,num,num
while(num!=0):
    count+=1
    num=num//10
while(temp1!=0):
    rem=temp1%10
    sum=sum+rem**count
    temp1=temp1//10

if sum==temp2:
    print("Its Armstrong")
else:
    print("Its not Armstrong")