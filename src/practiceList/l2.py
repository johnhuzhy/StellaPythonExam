#操作列表
#1.基本操作和str一样 len() + * in max() min()
alst=[22,33,'Java Sliver','Python','Java gold','日本語N1','DB'] 
print(len(alst))
print(alst+['Flower','sports'])
print(alst*3)
print('Python' in alst) #True
print('Java' in alst) #False

alst2=[1,23,45,67,89,90]
print(max(alst2))
print(min(alst2))

#2.修改列表元素 
#列表时可以修改的，字符串不可以修改
cities=['tokyo','beijing','shanghai','wuhan','shenzhen']
cities[-1]='guangzhou'
print(cities)
# str1='tokyo,wuhan'
# str1[-1:-5]='shanghai' #TypeError: 'str' object does not support item assignment 字符串不可以修改
# print(str1)

#3.增加列表元素 append
# 增加列表 extend
cities.append('横浜')
print(cities)
la=[1,23]
lb=[34,67,89]
la.extend(lb)
print(la)

#4.查询常用列表函数，用dir(list)  count(x) x在列表里出现的次数 index() 查找下标
lc=[1,2,3,34,4,3]
print(lc.count(3)) #2 次
print(lc.index(3))
#insert append和extendextend都是在列表末尾追加元素，insert可以指定位置追加
lc.insert(2,'java')
print(lc)
lc.insert(0,'Python')
print(lc)

#5.remove和pop 列表中的元素不仅能增加，还能被删除
all_user=['stella','qiuqiu','haruko','miyuki','HU','qiuqiu'] #列表元素可以重复
print(all_user)
all_user.remove('qiuqiu') #有重复的元素也是删除第一个
print(all_user) #['stella', 'haruko', 'miyuki', 'HU', 'qiuqiu']
all_user.pop(2)
print(all_user) #['stella', 'haruko', 'HU', 'qiuqiu']

all_user2=['stella','qiuqiu','haruko','miyuki','HU','qiuqiu']
# print(all_user2.remove('qiu')) #没有该元素时删除会报错
print(all_user2.pop()) #没有指定删除哪个时，默认删除最后一个。POP返回的是删掉的那个元素
print(all_user2)

#6.reverse 反转 列表是可变的，所以无需操作后用变量去接收，能直接改变
all_user2.reverse()
print(all_user2)

#7.sout 排序 从小到大 reverse只是反转，从后往前。
a=[1,4,6,0,3]
a.sort() #[0, 1, 3, 4, 6]
a.reverse() #[6, 4, 3, 1, 0]
print(a)

b=[1,4,6,0,3]
b.sort(reverse=True) #排序后再反转，就是从大到小排序的意思
print(b)

lst=['python','java','DB','php']
lst.sort(key=len) #按长度排序
print(lst)

#查看关键字
#  import keyword
#  keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']       
