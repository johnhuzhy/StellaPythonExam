'''
条件控制
'''
# elif 是else和if的结合。层级很多时，用elif。可以简化代码行数，减少嵌套
# input 进去的都是字符串，需要转换成int
a = input()
print('a is '+a)
print(type(a))
a = int(a)
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('Shopping')
