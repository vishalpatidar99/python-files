# Input : arr = [[1, 2, 2, 4, 3, 6],
#               [5, 1, 3, 4],
#               [9, 5, 7, 1],
#               [2, 4, 1, 3]]
# Output : [1, 2, 3, 4, 5, 6, 7, 9]
ip=[[1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]]
res=[]
for i in range(0, len(ip)-1):
    ip[i]=set(ip[i])
    res=ip[i].union(ip[i+1])
print(list(res))