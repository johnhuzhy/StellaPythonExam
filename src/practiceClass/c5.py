
#类与对象的变量查找顺序  先找对象的变量再找类对象
#__dict__查找变量方法、student1.__dict__  Student.__dict__
#self 在构造函数与类方法里参数时，一定要写上self 相当于Java中的this。在调用时不用给self赋值
class Student():
    #类变量
    name='qiqiyue'
    age=0
    sum=0

    #有参构造函数
    def __init__(self,name,age):
        #实例变量
        self.name=name
        self.age=age
        print(name)
        print(age)
        
    def print_file(self):
        print('name: '+self.name)
        print('age: '+str(self.age))


student1 = Student("stella",27)
student2 = Student("松島菜々子",29)
