# Input : test_list = [“gfgBest”, “forGeeks”, “andComputerScienceStudents”] 
# Output : [‘gfg Best’, ‘for Geeks’, ‘and Computer Science Students’] 
# Explanation : Words segregated by Capitals.

# Input : test_list = [“ComputerScienceStudentsLoveGfg”] 
# Output : [‘Computer Science Students Love Gfg’] 
# Explanation : Words segregated by Capitals. 
ip=['gfgBest', 'forGeeks', 'andComputerScienceStudents']
res=[]
for i in ip:
    a=""
    for j in range(len(i)):
        if i[j].isupper():
            a=a+" "+i[j]
        else:
            a+=i[j]
    res.append(a)
print(res)