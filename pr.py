
# s="123456789"
# temp=set()
# print(f"{s[0]} {s[1]} {s[2]}")
# print(f"{s[3]} {s[4]} {s[5]}")
# print(f"{s[6]} {s[7]} {s[8]}")
# print()
# for i in range(1,10):
#     if i%2!=0:
#         n=int(input("X's Term: "))
#         for j in range(3):
#             if n not in temp:
#                 s=s.replace(s[n-1],"x")
#                 temp.add(n)
#                 break
#             else:
#                 print()
#                 print("Reserved Try Again ")
#                 n=int(input("X's Term "))
#         print()
#         print(f"{s[0]} {s[1]} {s[2]}")
#         print(f"{s[3]} {s[4]} {s[5]}")
#         print(f"{s[6]} {s[7]} {s[8]}")
#         print()

#         t=0
#         d=0
#         a=0
#         y=""
#         if abs(s.count("x")-s.count("o"))>1:
#             a+=1
#             d+=1

#         if (s[0]==s[1]==s[2]=="x" or s[3]==s[4]==s[5]=="x" or s[6]==s[7]==s[8]=="x" or s[0]==s[3]==s[6]=="x" or s[1]==s[4]==s[7]=="x" or s[2]==s[5]==s[8]=="x" or s[0]==s[4]==s[8]=="x" or s[2]==s[4]==s[6]=="x"):
#             t+=1
#             d+=1
#             y = "x"

#         if (s[0]==s[1]==s[2]=="o" or s[3]==s[4]==s[5]=="o" or s[6]==s[7]==s[8]=="o" or s[0]==s[3]==s[6]=="o" or s[1]==s[4]==s[7]=="o" or s[2]==s[5]==s[8]=="o" or s[0]==s[4]==s[8]=="o" or s[2]==s[4]==s[6]=="o"):
#             y="o"
#             t+=1
#             d+=1

#         if t==2 or a==1:
#             print("It's Impossible")
#             exit()

#         if y=="x":
#             print("X win")
#             break
#         elif y=="o":
#             print("O win")
#             break

#         if t==0 and (any(chr.isdigit() for chr in s)):
#             print("Game is Not completed Yet")
#             d+=1
#         elif d==0:
#             print("Draw")

#     else:
#         n=int(input("O's Term: "))
#         for j in range(3):
#             if n not in temp:
#                 s=s.replace(s[n-1],"o")
#                 temp.add(n)
#                 break
#             else:
#                 print()
#                 print("Reserved Try Again ")
#                 n=int(input("O's Term "))
#         print()
#         print(f"{s[0]} {s[1]} {s[2]}")
#         print(f"{s[3]} {s[4]} {s[5]}")
#         print(f"{s[6]} {s[7]} {s[8]}")
#         print()

#         t = 0
#         d=0
#         a=0
#         y=""
#         if abs(s.count("x")-s.count("o"))>1:
#             a+=1
#             d+=1

#         if (s[0]==s[1]==s[2]=="x" or s[3]==s[4]==s[5]=="x" or s[6]==s[7]==s[8]=="x" or s[0]==s[3]==s[6]=="x" or s[1]==s[4]==s[7]=="x" or s[2]==s[5]==s[8]=="x" or s[0]==s[4]==s[8]=="x" or s[2]==s[4]==s[6]=="x"):
#             t+=1
#             d+=1
#             y = "x"

#         if (s[0]==s[1]==s[2]=="o" or s[3]==s[4]==s[5]=="o" or s[6]==s[7]==s[8]=="o" or s[0]==s[3]==s[6]=="o" or s[1]==s[4]==s[7]=="o" or s[2]==s[5]==s[8]=="o" or s[0]==s[4]==s[8]=="o" or s[2]==s[4]==s[6]=="o"):
#             y="o"
#             d+=1
#             t+=1

#         if t==2 or a==1:
#             print("It's Impossible")
#             exit()

#         if y=="x":
#             print("X win")
#             break
#         elif y=="o":
#             print("O win")
#             break

#         if t==0 and (any(chr.isdigit() for chr in s)):
#             print("Game is Not completed Yet")
#             d+=1
#         elif d==0:
#             print("Draw")


# dic={"Rohit":"India","Ram":"US","Mohan":"US","Aakash":"India","Hari":"India","Shyam":"US","gjggj":"pakistan"}
# value_list=set(dic.values())
# value_list=list(value_list)
# t=len(value_list)
# print(value_list)
# res={}
# i=0
# while(t>0):
#     l=[]
#     for k,v in dic.items():
#         if v==value_list[i]:
#             l.append(k)
#     res.update({value_list[i]:l})  
#     i+=1
#     t-=1
# print(res)