# 26个字母，随机取字母组成一个长度为100字符串
import random
import pdb
import re
def get_str():
    char_list = ['a','b','c','d','e','f','g','h','i']
    all_str = 'abcdefghi'
    str = ''
    for _i in range(100):
        str = str+random.choice(all_str)
    return str

def get_str1():
    char_list = ['a','b','c','d','e','f','g','h','i']
    str = ''
    for i in range(100):
        str += char_list[random.randint(0, len(char_list)-1)]
    return str

# str作为长字符串，给定短字符串abc，找到连续的abc短字串，获取到找到的abc短字串的数量，并给出a字符的位置

def get_substr(str_src, str_find):
    find_num = 0
    index_list = []
    compile_mode = re.compile(str_find)
    find_rs = compile_mode.search(str_src)
    flag = find_rs.span()[0]
    # pdb.set_trace()
    while find_rs.span()[0]:
        find_num += 1
        index_list.append(flag)
        find_rs = compile_mode.search(str_src[flag+1:])
        flag = find_rs.span()[0] + index_list[-1]
    return find_num,index_list

def find_substr(str_src, str_find):
    find_num = 0
    index_list = []
    index_f = 0
    for index in range(len(str_src)):
        # pdb.set_trace()
        while (index_f < len(str_find)):
            if str_src[index] != str_find[index_f]:
                index_f = 0
                break
            elif str_src[index] == str_find[index_f]:
                index +=1
                index_f +=1
            if index_f == len(str_find):
                find_num += 1
                index_list.append(index - len(str_find))
                index_f = 0
    return find_num,index_list

def find_str2(str_src, str_find):
    substr_list = str_src.split(str_find)
    find_num = len(substr_list) - 1
    find_list = []
    if find_num > 0:
        for i in range(len(substr_list)-1):
            num = len(substr_list[i])
            if i == 0:
                find_list.append(num)
            else:
                find_list.append(num + len(str_find) + find_list[i-1])
    return find_num,find_list

if __name__ == "__main__":
    # str = get_str1()
    # print(str)
    str = 'cdaadibiabcdbfaejcjadcecbfcdbifabchibhfjhiccjbjhfaeafigdhifdgcadjhjhhhgbcdaefdfidajijceiijhibbgjhgcb'
    find_num,find_list = find_str2(str, 'abc')
    print(find_num)
    print(find_list)