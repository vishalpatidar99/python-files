# The original list 1 is : [8, 5, 9, 11, 3, 7]
# The original list 2 is : [9, 11]
# The Grouped list is : [[8, 5], 9, 11, [3, 7]]
ip1=[8, 5, 9, 7,8,11, 3, 7,9,5]
ip2=[9, 11]
final_res=[]
res=[]
t2=0
for i in ip1:
    t=0
    t1=0
    for k in ip2:
        # import pdb;pdb.set_trace()
        if i!=k:
            t+=1
        if i==k:
            t1+=1
        if t==len(ip2):
            res.append(i)
            # print(res)
            t2+=1
        if t1==1 and t2>=1:
            final_res.append(res.copy())
            # print(final_res)
            res.clear()
            t2=0
        if t1==1:
            final_res.append(i)
            t1=0
final_res.append(res)
print(final_res)