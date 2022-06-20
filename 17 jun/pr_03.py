# Input : test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)] 
# Output : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)] 
# Explanation : 19 > 7 = 7 > 2, is order, hence reverse sorted by maximum element.

# Input : test_list = [(4, 5, 5, 7), (19, 4, 5, 3), (1, 2)] 
# Output : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 2)] 
# Explanation : 19 > 7 > 2, is order, hence reverse sorted by maximum element. 
ip=[(4, 5, 5, 7), (20, 3, 7, 4), (1, 4, 5, 3), (1, 2)]
ip.sort(reverse=True)
print(ip)