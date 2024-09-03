d = {'User': "Mark", 'Pass': "Phoenix"}
d.update({'id': 2398498})
# d.pop("id")
rem = d.popitem()
print(d)
print(type(d))
print(rem)
