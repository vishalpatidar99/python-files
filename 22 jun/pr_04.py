# Input : S = "the big dwarf only jumps"
# Output : Yes
# Each alphabet in the string S is occurred
# only once.

# Input : S = "geeksforgeeks" 
# Output : No
# Since alphabet 'g', 'e', 'k', 's' occurred
# more than once
s="geeksforgeeks"
s="".join(s.split())
print(s)
res=""
for i in s:
    if i not in res:
        res+=i   
print(res)
if res==s:
    print("YES")
else:
    print("NO")