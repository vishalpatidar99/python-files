# Input : {1, 2, 3}, n = 2
# Output : [{1, 2}, {1, 3}, {2, 3}]

# Input : {1, 2, 3, 4}, n = 3
# Output : [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]
from itertools import combinations


s={1, 2, 3, 4}
n = 3
sub_sets=combinations(s,n)
for i in sub_sets:
    print(set(i), end=" ")