#可变参数

def demo(*param):
    print(param)
    #tuple
    print(type(param))
 #第一种调用方式   
demo(1,2,3,4,5,6)

#不能直接传元组，变成二维元组了((1, 2, 3, 4, 5, 6),)
# demo((1,2,3,4,5,6))
#第二种调用方式 *a平铺把参数传进去
a=(1,2,3,4,5,6)
demo(*a)

#必须参数，可变参数,默认参数，
#没必要把参数设计这么复杂，这只是练习。实际上把参数设计简单比较好
def demo1(param1,*param,param2=2):
    print(param1)
    print(param)
    print(param2)


demo1('a',1,2,3,param2='param')   