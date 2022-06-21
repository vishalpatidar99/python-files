N,M=input().split(" ")
N=int(N)
M=int(M)
for i in range(1,N-1,2):
    print((".|."*i).center(M, '-'))
    
print(("WELCOME").center(M, '-'))

for j in range(N-2,0,-2):
    print((".|."*j).center(M, '-'))
    