from itertools import combinations
l=[(2,4),(6,7),(5,1),(6,10)]
print([(a1+b1,a2+b2) for (a1,a2),(b1,b2) in combinations(l,2)])
