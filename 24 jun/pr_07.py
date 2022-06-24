# Input : test_list = [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’ 
# Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’] 
# Explanation : All characters except G replaced by *

# Input : test_list = [‘G’, ‘F’, ‘G’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’ 
# Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’] 
# Explanation : All characters except G replaced by * 
ip=['G','F','G','I','S','B','E','S','T']
except_character='B'
changed_character='*'
for i in range(len(ip)):
    if ip[i]!=except_character:
        ip.pop(i)
        ip.insert(i, changed_character)
print(ip)
