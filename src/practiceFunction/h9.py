# {'bj': '32c', 'xm': '23c', 'sh': '31c'}
# <class 'dict'>
# def city_temp(**param):
#     print(param)
#     print(type(param))
# city_temp(bj='32c',xm='23c',sh='31c')

#.items 不能掉
# def city_temp(**param):
#     for key,value in param.items():
#         print(key,':',value)
# city_temp(bj='32c',xm='23c',sh='31c')

#*param传入的是一个元组，**param传入的是一个字典
#如果什么都不传，得到的是一个空字典{}
def city_temp(**param):
    for key,value in param.items():
        print(key,':',value)
a={'bj':'32c','xm':'23c'}       
city_temp(**a)