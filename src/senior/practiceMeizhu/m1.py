#20200623
#枚举，是一种数据类型
#枚举相比于字典和类，它的优势是不可变，不能重复
from enum import Enum
#枚举重在标签
class VIP(Enum):
    YELLOW=1
    GREEN=2
    BLACK=3
    RED=4

print(VIP.YELLOW)  #VIP.YELLOW
print(VIP.YELLOW.name) #得到标签名  YELLOW
print(VIP.YELLOW.value) #得到值 1
print(type(VIP.YELLOW))  #<enum 'VIP'>
print(type(VIP.YELLOW.name)) #<class 'str'>
#枚举类型，枚举的名字，枚举的类型
#遍历得到
for v in VIP:
    print(v)
# VIP.YELLOW
# VIP.GREEN
# VIP.BLACK
# VIP.RED