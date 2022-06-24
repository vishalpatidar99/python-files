# Input : test_tuple = ((1, ‘Gfg’, 2), (3, ‘best’, 4)), keys = [‘key’, ‘value’, ‘id’]
# Output : [{‘key’: 1, ‘value’: ‘Gfg’, ‘id’: 2}, {‘key’: 3, ‘value’: ‘best’, ‘id’: 4}]

# Input : test_tuple = test_tuple = ((1, ‘Gfg’), (2, 3)), keys = [‘key’, ‘value’]
# Output : [{‘key’: 1, ‘value’: ‘Gfg’}, {‘key’: 2, ‘value’: 3}]

ip=((1, 'Gfg'), (2, 3))
keys = ['key', 'value', 'id']
res=[]
for i in ip:
    r=dict(zip(keys,i))
    res.append(r)
print(res)