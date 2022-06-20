from operator import itemgetter
lis=[{"name":"Nandini","age":20},{"name":"Manish","age":18},{"name":"Nikhil","age":19}]
print(sorted(lis, key=itemgetter('age')))