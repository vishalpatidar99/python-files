d={"k1":[1,2,3],"k2":[4,5,2],"k3":[6,3,2,10,12,11]}
res=sorted({i for j in d.values() for i in j})
print(res)