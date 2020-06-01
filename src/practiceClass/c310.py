class People():
    sum=0
    def __init__(self,name,age):
        self.name=name #实例变量name
        self.age=age #实例变量age
        self.__class__.sum+=1 #操作类变量 sum
    
    def do_homework(self):
        print("*****************************DO MATH****************")