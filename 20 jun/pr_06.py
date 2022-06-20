      
# print(ip)
# Input : [4, 5, 5, 5, 3, 8]
# Output : 5
# Input : [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output : 1, 22

ip=[1, 1, 1, 64, 23, 64, 22, 22, 22,22,22,22]
res=[]
for i in range(1, len(ip)-1):
    if ip[i]==ip[i-1] and ip[i]==ip[i+1]:
        res.append(ip[i])
print(res)