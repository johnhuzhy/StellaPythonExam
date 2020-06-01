# 实现两个数字的相加  打印输入的参数
# return value  没有return的话，返回结果时none
# import sys
# sys.setrecursionlimit(10000000)

def add(x, y):
    result = x+y
    return result

# 自己掉用自己，会递归，
# 这里么有返回值，只有打印。所以后面把返回结果给b时，会出none


def print_code(code):
    print(code)


# 调用在定义后使用
a = add(1, 2)
b = print_code('sunshanshan')
# sunshanshan
# 3 None
print(a, b)
