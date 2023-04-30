# list
print("----next step is python list test----")
ii = [1,2,3,4,5]
print(type(ii))
print(isinstance(ii,list))
ii[2] = 5
print(ii)
ii.remove(2)
print(ii)
ii.pop(1)
print(ii)
del ii[1]
print(ii)
ii.clear()
print(ii)
ii.extend("aa")
print(ii)
ii.append("b")
print(ii.count("a"),ii.count("b"))
print(ii.index("a"))
ii.reverse()
print(ii)
ii.sort()
print(ii)
ii.sort(reverse=True)
print(ii)
ii.insert()
# tuple
print("----next step is python tuple test----")
jj = (1,2,3,4,5)
print(type(jj))
print(isinstance(jj,tuple))
# jj[2] = 5 # unable to edit tuple
print(jj)
# set
print("----next step is python set test----")
kk = {1,2,3,4,5}
print(type(kk))
print(isinstance(kk,set))
#kk[2] = 4 # unable to edit set
print(kk)
# dict
print("----next step is python dict test----")
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
