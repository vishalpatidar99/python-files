# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
ip=[0,1,2,3,4,5,5,9]
for i in range(0,len(ip)-1,2):
    ip[i+1],ip[i]=ip[i],ip[i+1]

print(ip)
