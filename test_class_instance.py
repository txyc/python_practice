# 类和实例的具体表现
# 1、类属性与实例属性的差异：属性不带下划线、带单下划线、带双下划线、前后都带下划线
# 2、私有方法、类方法和静态方法
# 3、@property的魔法函数使用
# 4、

import os

class Person()

class Student(object):
    def __init__(self, name, score):
        print("I'm a student")
        self.name = name
        self.score = score

if __name__=='__main__':
    print(os.listdir(os.getcwd())[1])
    f = open(os.listdir(os.getcwd())[1],'r')
    for line in f.readlines():
        print(len(line))
    
