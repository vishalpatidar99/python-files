# list of consecutive numbers list
l=[6,7,8,9,1,2,3,9,14,11]
l.sort()
res,final_result=[],[]
for i in range(1,len(l)):
    if l[i]-l[i-1]==1:
        res.append(l[i-1])
    else:
        res.append(l[i-1])
        final_result.append(res.copy())
        res.clear()

    # import pdb;pdb.set_trace()
    if i==(len(l)-1):
        if l[i]-l[i-1]==1:
            res.append(l[i])
            final_result.append(res.copy())
        else:
            # final_result.append(res.copy())
            # res.clear()
            res.append(l[i])
            final_result.append(res.copy())
    
print(final_result)