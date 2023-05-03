# coding:utf-8
# os.popen()方法将数组作为参数执行，返回系统命令行的执行结果，这里的参数输入和标准的cli系统不太相符
# subprocess模块可以通过模块方法将实际的cli系统命令输入直接执行，如下为其中的具体方法
#   subprocess.call()——执行输入命令行而不获取返回结果
#   subprocess.check_output()——执行输入命令行并获取返回结果
#   subprocess.Popen()——
import os
import subprocess
# popen返回文件对象，同open操作一样
f = os.popen(r"ls", "r")
l = f.read().split("\n")
print(l)
f.close()

rs = subprocess.call(['ls','-l'])
print(type(rs))
print(rs)
rs = subprocess.check_output(['ls','-l'])
print(type(rs))
print(rs)
child = subprocess.Popen(['ping','www.baidu.com'])
child.wait()
print('Finished')

rs = subprocess.call(['python','test_click.py',"hello1","2","mike"])
print(type(rs))
print(rs)