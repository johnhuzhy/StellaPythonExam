#静态方法 用@staticmethod，直接写参数，不需要用self或者cls，
#可以调用类变量，不能调用实例变量
#在调用静态方法时，用类名或者对象名点调用


class Student():
    # 类变量
    name = 'qiqiyue'
    age = 0
    sum = 0

    # 有参构造函数
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print("当前人数是:"+str(self.__class__.sum))  # 访问类变量

    @classmethod
    def print_sum(cls):
        cls.sum += 1
        # print(sum) 一定要用cls。sum    
        print(cls.sum)

    #静态方法 ，不需要self或者cls，调用时被类或者对象调用
    @staticmethod
    def add(x,y):
        #调用类变量
        print(Student.sum)
        print("This is a static method")


student1 = Student("stella", 27)
# 调用类方法
Student.print_sum()
#调用静态方法
Student.add(1,2)
student1.add(1,2)
