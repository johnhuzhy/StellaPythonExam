#默认参数
#默认参数没给的在调用时一定要给出来，不然会报错。给出的要换，直接在调用时重新赋值就可以
def print_student_files(name,gender='男',age=18,college='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')#int不能和字符串直接连接，需要转化成str
    print('我是'+gender+'生')
    print('我在'+college+'上学')

#么有给默认参数的调用时一定要给
print_student_files('福山')
print('******************************************************')
print_student_files('松岛')
print('******************************************************')
print_student_files('球球','男',14)
print('******************************************************')
print_student_files('花菜子','女',13)
print('******************************************************')
print_student_files('果果',age=15)
print('******************************************************')
#报错，调用时普通参数和关键字参数混合着写，要按照顺序写
# print_student_files('溜溜',gender='女',college='中山路小学',17)

print_student_files('溜溜','女',college='中山路小学',age=19)