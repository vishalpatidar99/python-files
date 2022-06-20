str="geeksforgeeks is best for geeks and cs"
wordlist=['geeks','for','cs']
replace='gfg'
res=' '.join([replace if i in wordlist else i for i in str.split()])
print(res)