# [['hello poor'], ['new'], ['world great']] [1, 2, 3]
# [[['hello', 1],['poor', 1]],[['new',2]],[['world',3],['great',3]]]

n = int(input('input number of time '))
l2 = []
for i in range(n):
    s = input('Enter all String with space in 3 part ')
    l2.append(s.split(' '))

l1 = input('Enter all itegers with space ').split(' ')


if len(l2) == len(l1):
    print(l2, l1)

else:
    print(l2, l1)
    print('not match please reenter')

final_res = []
for i in l2:
    res = []
    for j in i:
        a = []
        a.append(j)
        res.append(a)
    final_res.append(res)
# print(final_res)
k3 = []
temp = 0

for i in final_res:
    k1 = []

    for j in i:
        k2 = []
        for k in j:
            k2.append(k)
            k2.append(int(l1[temp]))
            # import pdb;pdb.set_trace()
        k1.append(k2)

    k3.append(k1)

    temp += 1

print(k3)
