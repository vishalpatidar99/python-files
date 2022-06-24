# Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
# Output : [‘learning’, ‘love’]
# Explanation : All elements with L as starting letter are extracted.
ip=["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
k = "l"
res=[]
for i in ip:
    for j in i.split(" "):
        if j.startswith(k):
            res.append(j)
print(res)