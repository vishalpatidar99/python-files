# Input : 14, 625, 498.002
# Output : 14.625.498, 002 
ip=input().split(" ")
s=""
for i in ip:s+=i
s=s.replace(",","a ")
print(s)
s=s.replace(".",",")
print(s)
s=s.replace("a",".")
print(s)

