# output="This is Matrix#  %!"
# s='''Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!'''
# M,N,i=7,3,0
# res=""
# while(i<N):
#     for j in range(i, len(s),N+1):
#         res+=s[j]
#     i+=1
# print(res)

t=0
res="This$#is% Matrix#  %!"
l=len(res)
final_result=res
for k in range(l):
    # import pdb;pdb.set_trace()
    if res[k].isalpha():
        if t>=1:
            res=res[:a-t+1]+" "+res[k:]
            t=0
        continue
    else:
        t+=1
        a=k
print(final_result)