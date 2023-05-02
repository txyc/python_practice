# 本篇主要用于介绍字符串的各种操作
# 字符串的拼接——+/join/format
# 字符串的分割——split
# 子串的检查——count/find/index/startswith/endswith
# 字符串格式化处理——ljust/rjust/center/strip/lstrip/rstrip
# 字符串大小写转化——lower/upper
# 编码解码处理——encode/decode
print("-" * 30)
print("字符串的拼接")
str1 = "12""34"
print(str1)
str2 = "12"+"34"
print(str2)
strli1 = ["12","34","56"]
str3 = "".join(strli1)
print(str3)
# print("".join([12,34])) # join拼接的对象必须是字符串数组
str4 = "name:{:s}\tage:{:d}".format("mike",21)
print(str4)
print("-" * 30)
print("字符串的分割")
str5 = "asdh asdghjsa sdhas"
strli2 = str5.split()
print(strli2)
str6 = "asdh,asdghjsa,sdhas"
strli3 = str6.split()
print(strli3)
str7 = str6[1:3]
print(str7)
str8 = str6[3:-1]
print(str8)
str9 = str6[1:10:2]
print(str9)
print("-" * 30)
print("子串的检查")
str10 = "asdkjhzfsafdjsafuyasxzbcxz"
print(str10.count("a"))
print(str10.find("a"))
print(str10.rfind("a"))
print(str10.find("a",5))
print(str10.find("a",7,11))
print(str10.index("a"))
print(str10.rindex("a"))
print(str10.startswith("a"))
print(str10.endswith("a"))
print("-" * 30)
print("字符串格式化处理")
str11 = "gdhsajgdsa".ljust(35)
str12 = "dashdjksahdsadjl".ljust(35)
str13 = "str11:{:s}xx\nstr12:{:s}xx".format(str11,str12)
print(str13)
str14 = "gdhsajgdsa".rjust(35)
str15 = "dashdjksahdsadjl".rjust(35)
str16 = "str14:{:s}xx\nstr15:{:s}xx".format(str14,str15)
print(str16)
str17 = "gdhsajgdsa".center(35)
str18 = "dashdjksahdsadjl".center(35)
str19 = "str17:{:s}xx\nstr18:{:s}xx".format(str17,str18)
print(str19)
str20 = str17.lstrip()
str21 = str17.rstrip()
str22 = str17.strip()
str23 = "str20:{:s}xx\nstr21:{:s}xx\nstr22:{:s}xx".format(str20,str21,str22)
print(str23)
print("-" * 30)
print("字符串大小写转化")
str24 = "adWDfd"
print("strlower:{:s}\nstrupper:{:s}".format(str24.lower(),str24.upper()))
print("-" * 30)
print("字符串编码与解码")
str25 = "Python语言练习"
print(str25.encode())
# print(str25.decode()) # 字符串本身不能被解码，只有被编码为其他编码类型时才能够被解码
print(str25.encode(encoding="gb2312").decode(encoding="gb2312"))