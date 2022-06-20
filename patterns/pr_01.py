row=7

for i in range(1,row+1):
    for j in range(1,6):
        if((j==1 and i!=1 and i!=row) or (i==1 and j!=1 and j!=5) or (i==row and j!=5 and j!=1) or (j==5 and i>3 and i!=row) or (i==4 and j!=2)):
            print("*", end="")
        else:
            print(" ", end="")
    print()