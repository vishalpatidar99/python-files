# The original list is : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# The String after join : gfgisbest
ip=[['g','f','g'],['i','s'],['b','e','s','t']]
final_result=""
for i in ip:
    res=''.join(i)
    final_result+=res
print(final_result)