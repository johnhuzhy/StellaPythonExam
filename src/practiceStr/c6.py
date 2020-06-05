#1.判断是否都是字母
str1='I love flower and 日本ドラマ'
print(str1.isalpha()) 

#2.分隔符
str1=str1.split(" ") #按照空格分隔字符串
print(str1) #得到一个list

#3.去掉字符串两头的空格
str2=' I am learning Python and Janpness '
str3=str2.strip() #去掉两头的空格
str4=str2.lstrip() #去掉左边的空格
str5=str2.rstrip() #去掉右边的空格
print(str3)
print(str4)
print(str5)

#4.字符串大小写的转换
str6='i love flower'.upper() #转为大写
print(str6)
str7='MY NAME IS SUNSHINE'.lower() #转为小写
print(str7)
print('#'*56)
#5.用jion拼接字符串 和+不一样
str8="I love flower and"
str8=str8.join('Python') #PI love flower andyI love flower andtI love flower andhI love flower andoI love flower andn
print(str8)
#jion(list)
b=['www','python','java','DB','janpness']
print('*'.join(b)) #用*拼接这个list

