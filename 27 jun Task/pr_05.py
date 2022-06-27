
stops=[['a', 'b', 6], ['a', 'c', 3], ['b', 'c', 1], ['c', 'b', 4], ['b', 'd', 2], ['c', 'd', 
8], ['c', 'e', 2], ['d', 'e', 9], ['e', 'd', 7]]
ip=['a','d']
related_stops=[]
for i in range(1):
    for j in i:
        if j==ip[0]:
            related_stops.append(stops[i])
            # for k in stops:
            #     if k==related_stops[1]:

# print(related_stops)
