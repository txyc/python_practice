# 类和实例的具体表现
# 1、类属性与实例属性的差异：属性不带下划线、带单下划线、带双下划线、前后都带下划线
# 2、私有方法、类方法和静态方法
# 3、@property的魔法函数使用
# 4、继承、多重继承、混入
# 5、单例模式

# 类属性在类定义和__init__函数之间定义，实例属性在__init__函数内定义
# 类属性为类本身所有，可以使用类名.属性名直接调用；实例属性为每一个具体的对象所有，使用对象名.属性名调用

# 不带下划线——表示公共属性和公共方法，
# 带单下划线——表示
# 带双下划线——表示私有属性和方法，只能在类的内部调用

# 静态方法——使用@staticmethod装饰，通过类名/实例名.方法名调用
# 类方法——使用@classmethod装饰，一般第一个参数使用对象cls，类似实例方法的self，通过类名.方法名调用
# 
class Person(object):
    aaa = "aaa"
    _bbb = "_bbb"
    __ccc = "_ccc"
    def __init__(self, name, age, taste):
        print("Hello world!")
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print("I'm _working")

    def __away(self):
        print("I'm __away")
        print(Person.__ccc)

class Student(Person):
    def __init__(self, name, age, grade, taste):
        print("I'm a student")
        self.name = name
        self._age = age
        self.grade = grade
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.grade)
        print(self.__taste)

    def _study(self):
        self._work()
        print(self._bbb)
        # print(self.__ccc) # 保护属性不允许子类使用
        # self.__away() # 保护方法也不允许子类调用

    @staticmethod
    def play():
        # print(aaa, name) # 静态方法不能调用类属性，实例属性
        print("Student play")

    @classmethod
    def exam(cls):
        # print(cls.name) # 类方法内不能调用实例属性
        print("Student exam:", cls.aaa)


if __name__=='__main__':
    print("不同类别的类属性的访问限制")
    print(Person.aaa, Person._bbb)
    # print(Person.__ccc) # 保护属性不允许外部直接访问
    print("-" * 30)
    
    print("不同类别的实例属性和方法的访问限制")
    person1 = Person("jack", 25, "badminton")
    print(person1.aaa, person1._bbb)
    person1.showperson()
    person1._work()
    # person1.__away() # 保护方法不允许外部直接访问
    print("-" * 30)

    print("继承类对象的实例属性和方法的访问限制")
    print(Student.aaa, Student._bbb)
    s1 = Student("Mike", 20, "freshman", "basketball")
    s1.showstudent()
    s1._study()
    s1._work()
    print("-" * 30)

    print("修改类属性的表现：")
    person1.aaa = "ttt"
    print("person1.aaa:",person1.aaa)
    print("Person.aaa:",Person.aaa)
    print("Student.aaa:",Student.aaa)
    Person.aaa = "sss"
    print("person1.aaa:",person1.aaa)
    print("Person.aaa:",Person.aaa)
    print("Student.aaa:",Student.aaa)
    Student.aaa = "kkk"
    print("person1.aaa:",person1.aaa)
    print("Person.aaa:",Person.aaa)
    print("Student.aaa:",Student.aaa)

    # __mro__函数用于查找类的继承关系链
    print(Student.__mro__)

    # 静态方法和类方法
    Student.play()
    s1.play()
    Student.exam()
    s1.exam()