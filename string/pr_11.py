def count(str1, str2):
    c,j=0,0
    for i in str1:
        if str2.find(i)>=0:
            c+=1

    print(f"Number of Commom letter in strings is: {c}")

str1=input("Enter first string ")
str2=input("Enter second string ")
count(str1,str2)
