#在实例方法中访问实例变量和类变量
#访问实例变量用self.  访问类变量用类名. 也可以self.__class__.

class Student():
    #类变量
    name='qiqiyue'
    age=0
    sum=2

    #有参构造函数
    def __init__(self,name,age):
        #实例变量
        self.name=name
        
        self.age=age
        print(self.name)  #访问实例变量最好加上self
        # print(name) #虽然结果和上面相同，但是他们不一样，这边用的是形参。如果形参name变成name1 就报错了
    
    def print_file(self):
        print('name: '+self.name)  #实例变量
        print(Student.sum) #访问类变量
        print(self.__class__.sum) #访问类变量

student1 = Student("stella",27)
student1.print_file()
