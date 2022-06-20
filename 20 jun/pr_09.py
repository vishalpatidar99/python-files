# Input :
# test_list = [(4, 5), (5, 6), (1, 3), (0, 0)]
# K = 0
# Output : [(4, 5), (5, 6), (1, 3)]
# Input :
# test_list = [(4, 5), (5, 6), (1, 3), (5, 4)]
# K = 5
# Output : [(4, 5), (5, 6), (1, 3), (5, 4)]

ip=[(4, 5), (5, 6), (1, 3), (5, 5)]
res=[]
for i in ip:
    if i[0]!=i[1]:
        res.append(i)

print(res)