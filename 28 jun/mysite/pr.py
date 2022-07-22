ip = [{'article':1,'id':3},{'article':2,'id':4},{'article':2,'id':6},{'article':3,'id':5}]
res = {}
for dictionary in ip:
    for key, value in dictionary.items():
        if key not in res:
            res.update({key:value})
        else:
            for key2, value2 in res.copy().items():
                if key==key2 and value!=value2:
                    res.update({key:value})
print(res)
    