# Python code to convert into dictionary
tup = [("akash", 10), ("gaurav", 12), ("anand", 14),
	("suraj", 20), ("akhil", 25), ("ashish", 30)]
di={} 
for a, b in tup:
    di.update({a:b})
print(di)
