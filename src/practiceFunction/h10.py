#变量作用域
#全局变量
c=50

def add(x,y):
    c=x+y
    print(c)
#变量作用域
add(1,2)
print(c)