# 类方法 操作与类相关的变量放在类方法里，虽然也可以放在实例方法里
# 类方法调用是类名.类方法名


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


student1 = Student("stella", 27)
# 调用类方法
Student.print_sum()
# student2 = Student("HU",27)
# student3 = Student("qiuqiu",27)
