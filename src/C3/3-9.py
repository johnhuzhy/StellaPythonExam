#java里有for(int i=0;i<10,i++) python里没有这个，用range()来控制
#range(0,10) 包前不包后，相当于i<10.如果不想一个一个显示，跳一个显示，range(0,10,2) 步长，相当于i+2

#0,1,2......9
# for x in range(0,10):
#     print(x)

#0,2,4,6,8
# for x in range(0,10,2):
#     print(x,end=' | ')

#递减 10 8 6 4 2 
# for x in range(10,0,-2):
#     print(x,end=' | ')


#题目 打印出1，3，5，，，
# a=[1,2,3,4,5,6,7,8]
# for x in range(1,9,2):
#     print(x,end=' | ')

a=[1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end=' | ')

#Python里也可以切片来取，不光是只能用循环 2代表步长
b=a[0:len(a):2]
print(b)