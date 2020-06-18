#_*_ coding:1234 _*_
#range(2,2)时不会走进去，break的是里面的一个循环，外面的继续走
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, n//x)
            break
    else:
        print(n, 'is a prime number')
