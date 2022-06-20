# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
ip=[9, 5, 6]
k=3
res=[(i,i**k) for i in ip]
print(res)