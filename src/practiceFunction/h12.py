c=1

def func1():
    # c=2
    def func2():
        # c=3
        print(c)
    func2()

# func1() #3 
# func1() # c=3被注释 2 
#作用域链 在函数内，如果有局部变量，就使用局部的，靠近利用，如果没有时才用全局的
func1() # c=2 c=3被注释 1
