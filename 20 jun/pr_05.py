# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output : [4, 3]
# Explanation : Both elements occur 4 times.

# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output : [4, 3, 6]
# Explanation : Occur 4, 3, and 3 times respectively.
from typing import Counter

ip=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k=3
print([t for t,v in dict(Counter(ip)).items() if v>3])