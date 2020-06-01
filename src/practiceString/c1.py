#字符串 用單引號和雙引號都可以
print("Stella")
print('ddoghhh')
#str int
print(type("123"))
print(type(123))

print("let's go")
# print('let's go') #報錯
print('let\'s go') #用反斜綫儅轉義符

#鏈接字符串 +
str1='20200602 '+'stella is studying'
print(str1)
# unsupported operand type(s) for +: 'int' and 'str' 報錯 整數和字符串不能一起拼接 
# +鏈接的兩個對象必須是同一類型
# str1=20200620+'stella is working'
# print(str1)

# str()函数
#TypeError: 'str' object is not callable 不能在用str 函数时有变量也叫str
str2=str(20200620)+'stella is working'
print(str2)

#int()函数
str3=int('98')+1
print(str3)

#repr() 返回一个字符串
str4='today is rainning'+repr(20200601)
print(str4)

#转义符
# \ 反斜线 \' 单引号  \'' 双引号 \n 换行 \t tab建   \r  回车符
print("address is http://www.google.com")
print("you can connect me by qq\\wechart\\gmail") #you can connect me by qq\wechart\gmail 第一个是转义符
