'''
条件控制
'''
# print(a);

# if else 选择性问题
# for while switch

mood = True
if mood:
    print('go to left')
    print('back away')
else:
    print('go to right')
print('back away')

a = 1
b = 2
c = 2
if a or b+1 == c:
    print('go to left')
else:
    print('go to right')

accunt = 'qiyue'
password = '123456'
print('please input account')
user_account = input()
print('please input password')
user_password = input()
if accunt == user_account and password == user_password:
    print('success')
else:
    print('fail')

a = True
# snippet 片段
if a:
    print('')
else:
    print('')


if True:
    print('')

if False:
    print('')

# 代码块 代码不要嵌套太多层，逻辑太多时，提取成函数
# if condition:
#     code1
#         code11
#         code22
#              code33
#              code44
#     code2
#     code3
# else:
#     code1
#     code2
#     code3


# elif 是else和if的结合。层级很多时，用elif。可以简化代码行数，减少嵌套
a = input()
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('Shopping')
