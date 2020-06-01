#成员可见性 公开和私有
#要想变成私有方法或者私有变量，需要在前加双划线(尾巴不能加)，私有方法不能被对象访问，报错 比如__marking() 
# 私有变量 是通过Python把私有变量改了它的名字，所以读不到 ，通过__dict__就可以看变量名
#student1.__score=-1 可以通过对象名.来创造新的变量，这里有赋值，所以会当作一个普通变量来看，因此print(student1.__score)可以 print(student2.__score)报错

class Student():

    sum=0

    # 有参构造函数
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
        print("当前人数是:"+str(self.__class__.sum))  # 访问类变量

    def marking(self, score):
        if score < 0:
            return "不能给同学打负分"
        self.score = score
        return self.name+'同学本次考试分数为:'+str(self.score)


student1 = Student("stella", 27)
res = student1.marking(99)
print(res)
student1.__score=-1 #可以实例化一个变量出来 通过student1.__score=-1 不报错 强行赋值 
print(student1.__dict__) #'_Student__score': 0原来的  '__score': -1现在强制赋值的
# print(student1.__score)

student2 = Student("球球", 1)
# print(student2.__score) #报错 'Student' object has no attribute '__score'、
print(student2.__dict__) #'_Student__score': 0 原来的通过改了一个名字所以现在就访问不了，要想访问，就要用它改过的名间接访问
