# The original list 1 is : ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
# The original list 2 is : [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
# The list after replacement : ['GksforGks', 'is', 'Best', 'For', 'Gks', '&', 'Comp Science']
ip1=['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
ip2=[['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
res=[]
for i in ip1:
    t=0
    for j in ip2:
        if j[0] in i:
            a=i.replace(j[0],j[1])
            res.append(a)
            t=1
    if t==0:
        res.append(i)
print(res)