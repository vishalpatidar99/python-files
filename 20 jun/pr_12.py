from typing import Counter


ip=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
res=Counter(ip[0])+Counter(ip[1])+Counter(ip[2])
print(res)