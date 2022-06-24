# Input : patterns = ['ape', 'apple', 
#                   'peach', 'puppy'], 
#           input = 'appel'
# Output : ['apple', 'ape']
from difflib import get_close_matches
print(get_close_matches(input("Enter for match "),['ape','apple','peach','puppy']))