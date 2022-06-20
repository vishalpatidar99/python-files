# Python – Convert Snake case to Pascal cases
tr=input("Enter string ")
res=str.replace("_"," ").title().replace(" ","")
print(res)