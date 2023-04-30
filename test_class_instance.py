import os

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
    
