# 本篇主要讲解随机数函数库的使用
# 主要涉及：
import random
print(random.randint(0,2)) # 返回值是一个数
print(random.choice("abcdefgh")) # 返回值是一个字符
print(random.choices("abcdefgh")) # 返回值是一个单个元素数组