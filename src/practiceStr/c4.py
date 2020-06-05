# 索引和切片
#索引下标从0开始
lang="my name is sunshanshan,my old is 27"
#通过索引找字符串
str1=lang[1]
str2=lang[8]
print(str1)
print(str2)
#通过字符串找索引 打出的是第一个出现的字母
print(lang.index('m'))
print(lang.index('i'))

#取得多个字符，用切片.包前不包后
str3=lang[1:13]  #y name is su
print(str3)
str4=lang[5:] #me is sunshanshan,my old is 27 从下标5开始截取到最后
print(str4)
str5=lang[:]#得到所有字符串 相当于复制了原来一份，id也相同
print(id(str5))
print(id(lang))
print(str5)
str6=lang[:16] #my name is sunsh 也适用不包括尾巴 a是16，所以打出a之前的 从前开始截取，到下标16为止，不包括16
print(str6)
str7=lang[-1] #负数表示从后往前取，代表是位数了，不是下标  7
print(str7)
str8=lang[4:-4]  #ame is sunshanshan,my old i 从下标4开始往后取，取到倒数第四位为止 ，不包括第四位的s，也符合包前不包后
print(str8)

print('#'*33)
lang2="0123456789abcdef"
# lang3="hello,Java,Pytho,C#"
str9=lang2[::1]  #1
print(str9)
str9=lang2[::2]  #2
print(str9)
str9=lang2[::4]  #4
print(str9)
str9=lang2[::-1]  #-1
print(str9)
str9=lang2[::-2]  #-2
print(str9)

print('#'*33)
#a和c指向同一个内存地址
a="Study python"
c=a
print(id(a))
print(id(c))


