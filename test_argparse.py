# argparse也是Python的内建模块，使用方式相对复杂一点，类似re模块的使用方式：
# 先使用ArgumentParser创建参数模型，再使用add_argument指定需要输入的参数
# 相比于argv，argparse接受参数时，可以使用类似键值对的方式显示地标明参数的含义，而且可以正确地指定参数的类型
import os
import argparse

parser = argparse.ArgumentParser(usage='test',description='please input paras')
parser.add_argument('-n','--name',dest='name',type=str,default='Mike',help='please imput your name')
parser.add_argument('-a','--age',dest='age',type=int,default=12,help='please imput your age')
args = parser.parse_args()

def hello(name, age):
    print("hello,{:s}!".format(name))
    print("I'm {:d} years old.".format(age))

if __name__ == "__main__":
    name = args.name
    age = args.age
    hello(name,age)
    os.system("pause")
