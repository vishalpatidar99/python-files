# Python Program to print all Possible Combinations from the three Digits
# ip=[6,8,7]
# for i in range(len(ip)):
#     for j in range(len(ip)):
#         for k in range(len(ip)):
#             if(i!=j and j!=k and k!=i):
#                 print(ip[i],ip[j],ip[k])
from itertools import permutations
print([i for i in list(permutations([1,2,3],3))])