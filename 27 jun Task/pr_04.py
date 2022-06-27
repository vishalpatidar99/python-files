term=list(input("Enter ").split(" "))

for i in range(2,len(term)):
    if term[0]>=term[1]:
        term[1]+=term[i]
    else:
        term[0]+=term[i]
if term[0]>=term[1]:
    print("A is Win")
else:
    print("B is Win")
