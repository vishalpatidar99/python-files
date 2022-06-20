# n=int(input("Enter number of element "))
# l=[]
# for i in range(n):
#     ele=int(input("Enter element "))
#     l.append(ele)
# print(l)
# l = [5, 10, 5,10,20, 10, 5]
l=[5,10,5,5,20]
count_5=0
count_10=0
c = 0
res = []
for m in l:
    if m == 5:
       res.append(m)
       count_5+=1
    elif m>5:
        if m==10 and count_5>=1:
            res.remove(5)
            res.append(m)
            count_5-=1
            count_10+=1
            # print(res)
        elif m==20 and count_5>=3:
            res.remove(5)
            res.remove(5)
            res.remove(5)
            res.append(m)
            count_5-=3
        elif m==20 and count_5>=1 and count_10>=1:
            res.remove(5)
            res.remove(10)
            res.append(m)
            count_5-=1
            count_10-=1
        else:
            break
    else:
        break
    c+=1

print(res)
if c != (len(l)):
    print(False)
else:
    print(True)
