def demo():
    global c
    c=2
#利用global，可以把局部变量变成全局用，但是事先得调用这个函数
demo()
print(c)