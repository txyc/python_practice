import sys

def hello(name, age):
    print("hello,{:s}!".format(name))
    print("I'm {:s} years old.".format(age))

if __name__ == "__main__":
    file_name = sys.argv[0]
    name = sys.argv[1]
    age = sys.argv[2]
    hello(name,age)

