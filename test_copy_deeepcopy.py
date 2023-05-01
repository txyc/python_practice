# 浅拷贝：将原对象或者原数组的引用直接赋值给新对象或者新数组，新对象、新数组只是原对象的一个引用
# 深拷贝：创建一个新的对象和数组，将元对象的各项属性的“值”拷贝过来
# 浅拷贝和深拷贝在不可变对象拷贝上的表现是相同的
# 浅拷贝和深拷贝在可变对象的拷贝上，在可变对象的子对象是不可变对象时，二者的表现也是相同的；
# 但是当可变对象的子对象时可变对象，就能发现浅拷贝的子对象与原对象的子对象表现一致
# 深拷贝的子对象则完全新建了一个对象

import copy

print("不可变对象的深浅拷贝的差异")
a = 123
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
a = 234
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
print("-" * 30)

a = "abcdf"
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
a = "abcdgs"
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
print("-" * 30)

print("可变对象的深浅拷贝的差异")
a = [1,2,3,4,5,[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
print("-" * 30)

a[1] = 6
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
print(id(a[1]))
print(id(b[1]))
print(id(c[1]))
print("-" * 30)

a[5][1] = 5
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
print(id(a[5]))
print(id(b[5]))
print(id(c[5]))
print("-" * 30)