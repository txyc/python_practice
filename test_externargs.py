import sys
import argparse

#text = sys.argv[1]
#print(text)
parser = argparse.ArgumentParser(usage='test',description='please input paras')
parser.add_argument('-n','--name',dest='name',type=str,default='hello world',help='please imput paras')
args = parser.parse_args()
username = args.name
print(username)


