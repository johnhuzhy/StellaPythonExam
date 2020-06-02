#序列:字符串 列表 元组
#列表
l1=[22,33,'5','Java','I love flower and python']
print(type(l1)) #<class 'list'>

#索引和切片 找字符串
print(l1[1])
#print(l1[6]) #IndexError: list index out of range 越界
print(l1[4])
print("#"*56)
print(l1[1:]) #[33, '5', 'Java', 'I love flower and python']
print("#"*56)
print(l1[1:4]) #[33, '5', 'Java'] 包前不包后
#可以对列表元素做2次切片
print("#"*56)
print(l1[4][2:8])  #love f

#index()  根据字符串找索引
# print(l1.index('java')) #ValueError: 'java' is not in list
print(l1.index('Java')) #3

#切片是负数时，代表位数从后往前找 当区间进行找时也符合包前不包后
print(l1[-2:]) #['Java', 'I love flower and python']
print(l1[:-3]) #[22, 33]
print(l1[-3:-1]) #['5', 'Java']
print(l1[-1:-3]) #空值  序列都是从左向右读取，此处从右向左读，返回空值
print(l1[-1])  #I love flower and python
print("#"*56)

#切片3个
alst=[0,1,2,3,4,5,6,7,8,9]
print(alst[::1]) #[0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(alst[::2])
print(alst[::3])
#反转 -代表从右开始读
print(alst[::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(alst[::-2]) #易错 [9, 7, 5, 3, 1]
print(alst[::-4]) #[9, 5, 1]
#反转推荐使用reversed ,不用忘了写list(),将迭代对象转化为列表显示
a=list(reversed(alst))
print(a)


