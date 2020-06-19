# for循环 主要用来遍历循环 序列或者集合，字典
# 后面的else用得少
# for里的else 会在for循环完了后执行，while里的else，是当条件为false时执行，一般for和while里的else用的少


# a=['apple','orange','banana','grape']
# for x in a:
#     print(x )

print('**************************************')
b = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for y in b:
    for z in y:
        print(z)  # 被纵向打印出来
        print(z, end=' ')  # 被横向打印出来
else:
    print('fruit is gone')
