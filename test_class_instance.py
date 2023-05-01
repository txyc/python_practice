# 类和实例的具体表现
# 1、类属性与实例属性的差异：属性不带下划线、带单下划线、带双下划线、前后都带下划线
# 2、私有方法、类方法和静态方法
# 3、@property的魔法函数使用
# 4、继承、多重继承、混入

class Person(object):
    aaa = "1"
    _bbb = "2"
    __ccc = "3"
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

if __name__=='__main__':
    print(Person.aaa, Person._bbb)
    # print(Person.__ccc) # 保护属性不允许外部直接访问
    print("-" * 30)
    
    person1 = Person("jack", 25, "badminton")
    person1.showperson()
    person1._work()
    # person1.__away() # 保护方法不允许外部直接访问
    print("-" * 30)

    print(Student.aaa, Student._bbb)
    s1 = Student("Mike", 20, "freshman", "basketball")
    s1.showstudent()
    s1._study()
    print("-" * 30)