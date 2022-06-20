# The original list 1 is : [‘Gfg’, ‘is’, ‘best’]
# The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
# The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’]
ip=['gfg', 'is','best']
l=[0,1,2,1,0,0,2,1,1,2,0]
print([ip[i] for i in l])