# Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 0 
# Output : [4, 4, 2] 
# Explanation : 5 – 1 = 4, hence 4. 
 

# Input : test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)], K = 2 
# Output : [2, 4, 5] 
# Explanation : 8 – 3 = 5, hence 5. 
ip=[(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
k= 1
res=[]
for i in range(len(ip)):
    for j in range(len(ip)):
        if j-i==1:
            t=abs(ip[i][k]-ip[j][k])
            res.append(t)
print(res)
