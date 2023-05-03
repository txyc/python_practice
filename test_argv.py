# argv是python的内置模块，用法也相对简单，类似顺序式输入参数的函数
import os
import sys

def hello(name, age):
    print("hello,{:s}!".format(name))
    print("I'm {:s} years old.".format(age))

if __name__ == "__main__":
    file_name = sys.argv[0]
    name = sys.argv[1]
    age = sys.argv[2]
    hello(name,age)
    os.system("pause")

