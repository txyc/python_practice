# Python中通过re模块完成正则表达式的匹配操作
# 通过re.compile创建匹配模式，然后使用search/match/findall调用匹配模式完成正则表达式的匹配动作
# 如果匹配模式中使用()来对匹配模式进行分组，则部分返回结果会变成元组的形式
# search方法——可以从待匹配字串中的任意位置开始匹配，默认返回第一个re.Match对象
# match方法——必须从待匹配字串头部开始匹配，默认返回第一个re.Match对象
# findall函数——返回所有的匹配字段
import re
strtest = "134-56123-456798-123"
strtest1 = "13456123-456798-123"
print("使用compile创建匹配模式")
match_mode = re.compile(r"(\d\d\d)-(\d\d\d)")
print(id(match_mode))
print(type(match_mode))
print("使用search调用匹配模式完成正则表达式匹配")
result = match_mode.search(strtest)
print(result)
print(type(result))
print(result.groups())
print(type(result.groups()))
print(result.group(0))
print(type(result.group(0)))
print(result.group(1))
print(type(result.group(1)))
print("使用match调用匹配模式完成正则表达式匹配")
result1 = match_mode.match(strtest)
print(result1)
print(type(result1))
print(result1.groups())
print(type(result1.groups()))
print(result1.group(0))
print(type(result1.group(0)))
print(result1.group(1))
print(type(result1.group(1)))
print("match方法必须从头开始匹配，如果字串头不包含匹配模式，则匹配失败")
result2 = match_mode.match(strtest1)
print(result2)
print("使用findall调用匹配模式完成正则表达式匹配")
result3 = match_mode.findall(strtest)
print(result3)
print(type(result3))