#字符串基本操作 len(object) + * in max min
str1="Hello Shanshan"
print(len(str1))

print('h' in str1)

print("#"*56)

print(max(str1))

# he said,"it's nothing".
print("he said,\"it's nothing\".")
print(r'''he said,"it's nothing".''')

#chr 把数字转为字符串，ord把字符转为数字
str1=chr(68)
str2=ord('b')
print(str1,str2)

#str是不变的，使用了方法后一定要用个值来接收，不然是不会变的。format()传参
str3='I Like {0} and {1}'
str3=str3.format("dorama","flower")
print(str3)

#dir(str) 是查看字符串的方法
print(dir(str))