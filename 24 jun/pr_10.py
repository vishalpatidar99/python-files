# Input : test_list1 = [“Gfg”, “is”, “not”, “best”, “and”, “not”, “CS”], 
# test_list2 = [“Its ok”, “all ok”, “wrong”, “looks ok”, “ok”, “wrong”, “thats ok”], sub_str = “ok” 
# Output : [‘Gfg’, ‘is’, ‘best’, ‘and’, ‘CS’] 

ip1=['gfg','is','not','best','and','not','CS']
ip2=['its ok','all ok','wrong','looks ok','ok','wrong','thats ok']
k="ok"
res=[]
for i in range(len(ip2)):
    if k in ip2[i].split(" "):
        res.append(ip1[i])
print(res)
