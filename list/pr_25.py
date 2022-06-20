# Python | Remove empty tuples from a list
list=[34,23,12,(),65,()]
res=[i for i in list if i!=()]
print(res)