# input()
#输入的数字是字符串，需要转换成int后再做加减，再打印时要把int 转成str
name = input("what's your name?")
age = input("How old are you?")
after_age = int(age)+3
print("my name is "+name)
print("today my old is "+str(age))
print("after 3 years my old is "+str(after_age))

