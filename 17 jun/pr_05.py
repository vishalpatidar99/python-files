# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

# Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
# Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]
ip=[('452', 10), ('256', 20), ('100', 5), ('135', 15)]
for i in range(len(ip)):
    for j in range(len(ip)):
        if ip[i][1]<ip[j][1]:
            ip[i],ip[j]=ip[j],ip[i]
print(ip)