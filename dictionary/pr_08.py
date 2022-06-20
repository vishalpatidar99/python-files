from itertools import product
d = {'month' : [1, 2, 3],'name' : ['Jan', 'Feb', 'March']}
res=dict(zip(d['month'],d['name']))
print(res)