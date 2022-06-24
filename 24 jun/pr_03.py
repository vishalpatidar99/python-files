#Conversion of numeric words to nummber
num=input("Enter numeric words ").split(" ")
help_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero' : '0'}
res=''
temp=""
for i in num:
    for k,v in help_dict.items():
        if k==i:
            res+=v
    temp+=i+" "
print(temp+" = "+res)