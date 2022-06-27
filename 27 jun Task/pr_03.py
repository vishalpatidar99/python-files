r1=int(input("Enter Starting room "))
r2=int(input("Enter Ending room "))
floors=0

if r2-r1>0:
    for i in range(r1,r2):
        if (i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90):
            floors+=1
else:
    for i in range(r1-1,r2-1,-1):
        if i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90:
            floors+=1
print(floors)