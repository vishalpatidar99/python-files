input_string="abbbcccdaa"

#initialize empty string and take count variable as 0 value for count characters
result=''
count=0

for i in range(1,len(input_string)):

    # Compared characters of previous index and current index if true increase count
    if input_string[i-1] == input_string[i]:
        count+=1

    #if not equal add this character in empty string first and then increase count and then add count in result string
    if input_string[i-1] != input_string[i]:
        result+=input_string[i-1]
        count+=1
        result+=str(count)
        count=0

    #in this scenario last element will skip, so this condition will keep it and check this is matching with previous character or not and add with it's behaviour
    if i==(len(input_string)-1):
        result+=input_string[i]
        count+=1
        result+=str(count)
        
print(result)