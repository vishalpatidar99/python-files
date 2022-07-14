# routers=[1,2,3,4,5,6]
ip = [1,2,3,5,2,1]
inbound = 1
outbound = 0
res={}
res.update({ip[0]:inbound+outbound})

for i in range(1,len(ip)-1):
    outbound+=1
    res.update({ip[i]:inbound+outbound})
    outbound = 0

res.update({ip[len(ip)-1]:inbound+outbound})
print(res)
