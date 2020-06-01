#序列解包与链式赋值

a=1
b=2
c=3

a,b,c=1,2,3

d=1,2,3
print(type(d)) # tuple
#序列解包
a,b,c=d

#c去掉的话会报too many values to unpack (expected 2) ,左边个数和右边要相等
a,b,c=[1,2,3]

x=1
y=1
z=1
#也可以这么定义
x=y=z=1