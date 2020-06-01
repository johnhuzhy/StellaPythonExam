#类最基本作用是封装代码
#类里不要去调用代码，对类的调用放在外面
#实例化
#和Java不同点总结
#在方法里即使是无参方法，也要写self ，在用的时候，要self.调用
#实例化时不需要用new
class Student():
    name=''
    age=0

    #无参构造函数
    def __init__(self):
        print('student')

    #有参构造函数
    def __init__(self,name,age):
        name=name
        age=age
        

    def print_file(self):
        print('name: '+self.name)
        print('age: '+str(self.age))


# student = Student()
# student.print_file()
student2 = Student("stella",27)

print(student2.__dict__)#dict是打出对象变量
print(Student.__dict__)#dict是打出类变量
print(student2.name)  #打印出最初的空字符
#python里类与对象的变量查找顺序 先查找对象的变量，在查找类的变量
