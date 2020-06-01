#繼承父類
#super關鍵字
from lei.c310 import People
#继承了People类
class Student(People):
    def __init__(self,school,name,age):
        self.school=school
        # People.__init__(self,name,age)#self不能掉，不然会报错，找不到name，age
        #使用super調用父類的方法
        super(Student,self).__init__(name,age)


    def do_homework(self):
        super(Student,self).do_homework()
        print('English homework')

student1=Student()
print(student1.sum)

student2=Student("人民路小学","Stella",20)