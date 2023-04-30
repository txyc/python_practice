a = {}
print(type(a))
print(isinstance(a,dict))
print(a)
a = dict((['one',1], ['two',2], ['three',3]))
print(a)
print(a.values())
a.pop("three")
for k,_v in a.items():
    print(k)
