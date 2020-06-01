# def demo():
#     c=10  #局部变量
# #NameError: name 'c' is not defined
# print(c)


def demo1():
    c=50
    for i in range(0,3):
        a='abc'
        c+=1
    print(c)
    #和Java不同之处，在Java里不能调用for循环里定义的变量，如果想要用，就先要提到for循环外，在里面改变。然后for循环外就可以调用了
    #python里for循环外直接可以调用for循环里定义的变量。因为python没有块级作用域，只有函数作用域
    print(a)
demo1()




