from itertools import permutations
str="ABC"
permlist=permutations(str)

for perm in list(permlist):
    print(''.join(perm))