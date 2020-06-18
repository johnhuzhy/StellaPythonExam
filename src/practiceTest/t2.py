# 加减乘除
print("请输入第一个整数:")
a = input()
a = int(a)
print("请输入第二个整数:")
b = input()
b = int(b)

# 加


def add(a, b):
    print("{0}和{1}相加、結果：{2}".format(a, b, a+b))


# sub
def sub(a, b):
    print("{0}和{1}相减、結果：{2}".format(a, b, a-b))

# 乘积


def chengji(a, b):
    print("{0}和{1}乘积、結果：{2}".format(a, b, a*b))

# 除


def chu(a, b):
    if(b == 0):
        print("除数为0，不能相除")
    else:
        print("{0}和{1}相除、結果：{2}".format(a, b, a/b))

# 取余


def quyu(a, b):
    if(b == 0):
        print("除数为0，不能相除")
    else:
        print("{0}和{1}取余、結果：{2}".format(a, b, a%b))

# 咪
def mici(a, b):
    print("{0}和{1}幂次、結果：{2}".format(a, b, a**b))


add(a, b)
sub(a, b)
chengji(a, b)
chu(a, b)
quyu(a, b)
mici(a, b)