# The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
# The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
ip=[[4,1,6],[7,8],[4,10,8]]
for i in ip:
    i.sort(reverse=True)
print(ip)