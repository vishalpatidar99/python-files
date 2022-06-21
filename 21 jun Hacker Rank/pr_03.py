t=5
for i in range(1,t*2,2):
    print(('H'*i).center(t*2, ' '))
for i in range(t+1):
    print(("H"*t).center(t*2, ' ')+"          "+("H"*t).center(t*2, ' '))
for i in range(t//2+1):
    print(("H"*t*5).rjust(t*5+2, ' '))
for i in range(t+1):
    print(("H"*t).center(t*2, ' ')+"          "+("H"*t).center(t*2, ' '))
for i in range(t):
    print((("H"*(t-i-1)).rjust(t)+"H"+("H"*(t-i-1)).ljust(t)).rjust(t*6))
