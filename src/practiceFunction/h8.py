#关键字可变参数

def squsum(*param):
    sum=0
    for i in param:
        sum+=i*i
    print(sum)

squsum(1,2,3)