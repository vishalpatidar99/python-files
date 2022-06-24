# test_list1 = [ [1, 2], [3, 4], [5, 6] ]
# test_list2 = [ [3, 4], [5, 7], [1, 2] ]
#op=[[5,6],[5,7]]
ip1=[[1, 2],[3, 4],[5, 6]]
ip2=[[3, 4],[5, 7],[1, 2]]
# ip1.extend(ip2)
# print(ip1)
res=[]
for i in ip1:
    if i not in ip2:
        res.append(i)
for i in ip2:
    if i not in ip1:
        res.append(i)
print(res)