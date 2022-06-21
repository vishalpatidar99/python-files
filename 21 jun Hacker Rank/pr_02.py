st = input("Enter String")
print()
t1=any(s.isalnum() for s in st)
t2=any(s.isalpha() for s in st)
t3=any(s.isdigit() for s in st)
t4=any(s.islower() for s in st)
t5=any(s.isupper() for s in st)
    
if t1 is True:
    print(True)
else:
    print(False)
    
if t2 is True:
    print(True)
else:
    print(False)
    
if t3 is True:
    print(True)
else:
    print(False)
    
if t4 is True:
    print(True)
else:
    print(False)
    
if t5 is True:
    print(True)
else:
    print(False)