# Python | Count occurrences of an element in a list
list=[23,10,42,10,10,43,3]
x,c=10,0
for i in list:
    if x==i:
        c+=1
print(c)