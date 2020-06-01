#类最基本作用是封装代码
#类里不要去调用代码，对类的调用放在外面
#实例化
#和Java不同点总结
#在方法里即使是无参方法，也要写self ，在用的时候，要self.调用
#实例化时不需要用new
#类变量与实例变量 类变量与类相关的变量，实例变量与对象相关的变量
class Student():
    #类变量
    name='qiqiyue'
    age=0

    #有参构造函数
    def __init__(self,name,age):
        #实例变量
        self.name=name
        self.age=age
        
    def print_file(self):
        print('name: '+self.name)
        print('age: '+str(self.age))


student1 = Student("stella",27)
student2 = Student("松島菜々子",29)
print(student1.name)
print(student2.name)
print(Student.name)  