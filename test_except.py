# Python中异常的处理主要是try-except-else-finally的样式
# 另外还需要关注不同代码块中存在return语句的处理方式
# try:
#     代码块执行，正常执行时会执行else/finally代码块，如果try代码块带return，会跳过else直接执行finally
# except:
#     发生异常，执行这块代码
# else:
#     try代码块中不带return，且未发生异常时，执行这块代码
# finally:
#     无论try代码块是否发生异常，是否带return，都执行这块代码

def test_except1():
    print("try执行OK时，except代码块不执行，else和finally代码块执行")
    try:
        print("hello try")
    except:
        print("hello except")
    else:
        print("hello else")
    finally:
        print("hello finally")

def test_except1_return1():
    print("try执行OK带return时，except和else代码块不执行，finally代码块执行")
    try:
        print("hello try")
        return 0
    except:
        print("hello except")
    else:
        print("hello else")
    finally:
        print("hello finally")

def test_except1_return2():
    print("try执行OK，else代码块带return时，except不执行，else和finally代码块执行")
    try:
        print("hello try")
    except:
        print("hello except")
    else:
        print("hello else")
        return 0
    finally:
        print("hello finally")

def test_except2():
    print("try执行异常时，else代码块不执行，except和finally代码块执行")
    try:
        print("hell try")
        print(1/0)
    except:
        print("hello except")
    else:
        print("hello else")
    finally:
        print("hello finally")

def test_except2_return1():
    print("try执行异常，except带return时，else代码块不执行，except和finally代码块执行")
    try:
        print("hell try")
        print(1/0)
    except:
        print("hello except")
        return 0
    else:
        print("hello else")
    finally:
        print("hello finally")

if __name__ == "__main__":
    test_except1()
    test_except1_return1()
    test_except1_return2()
    test_except2()
    test_except2_return1()