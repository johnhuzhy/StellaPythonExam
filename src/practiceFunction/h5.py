#必须参数与关键字参数
#必须参数与关键字参数的区别在函数的调用上
def add(x, y):
    #形式参数 形参
    result = x+y
    return result
#实参 按照顺序给，x=3,y=2  
d=add(3,2)
d=add(3)#报错，个数不对

#关键字参数 指定传进去的哪个是x，y，方便阅读代码
C=add(y=3,x=2)