# 列表、元组、集合、字典的特征差异
# 有序和无序的含义——是否可用下标提取序列值
# 可变和不可变的含义——数据标识的实际值改变后，数据类型的id是否变化，变化则为不可变类型，不变则为可变类型
# 有序序列：字符串、列表、元组
# 无序序列：集合
# 数值和字典不属于序列
# 可变的数据类型：列表、字典、集合
# 不可变数据类型：数值、字符串、元组、布尔值
# list
print("----next step is python list test----")
ii = [1,2,3,3,4,4,5]
print(type(ii))
print(isinstance(ii,list))
print(id(ii))
ii[2] = 5
print(ii)
print(id(ii))
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
ii.insert(1,"t")
print(ii)
ii.extend("cc")
print(ii)
print(ii.count("c"))
print(ii.index("c"))
print(max(ii))
print(min(ii))
print(len(ii))
print(sorted(ii))
# tuple
print("----next step is python tuple test----")
jj = (1,)
print(type(jj))
print(isinstance(jj,tuple))
print(id(jj))
jj = (1,2,4,4,4,3,3,3,5,5,5)
print(id(jj))
# jj[2] = 5 # unable to edit tuple
print(jj)
print(max(jj))
print(min(jj))
print(len(jj))
print(sorted(jj))
print(jj.__sizeof__())
print(ii.__sizeof__())
# set
print("----next step is python set test----")
kk = {1,2,4,4,4,3,3,3,5,5,5}
print(type(kk))
print(isinstance(kk,set))
#kk[2] = 4 # unable to edit set
print(kk)
kk.add(6)
kk.update([7,8])
print(kk)
# print(kk[2]) # unable to get index value
kk.remove(4)
print(kk)
kk.clear()
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
del a['two']
print(a)
a.clear()
print(a)
a = {'one':1, 'two':2, 'three':4, 'three':3}
print(a.keys())
print(a.values())
print(a.get('one'))
