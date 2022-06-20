import string
import time
import random

possibleCharacter=string.ascii_lowercase+string.ascii_uppercase+string.digits+' .?!@#$%^&*()<>?\/:;'
t='g e e k'
attemptThis=''.join(random.choice(possibleCharacter) for i in range(len(t)))
attemptNext=''
completed=False
iterations=0

while completed==False:
    print(attemptThis)
    attemptNext=''
    completed=True

    for i in range(len(t)):
        if attemptThis[i]!=t[i]:
            completed=False
            attemptNext+=random.choice(possibleCharacter)
        else:
            attemptNext+=t[i]
    
    iterations+=1
    attemptThis=attemptNext
    time.sleep(0.1)

print(iterations, "Iterations")