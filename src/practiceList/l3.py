#列表是苦力工，什么类型元素都可以装
#多维列表 
#这个列表的元素是另外四个列表
matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,14]]
print(matrix[0][1]) #2
print(matrix[3][3]) #14

mult=[[1,2,3],['a','b','c'],'d','e',{5,6,7,8},(9,10)]
# print(mult[3][1]) # 报错
print(mult[3][0]) #e
# print(mult[4][3]) #TypeError: 'set' object is not subscriptable 集合是没有下标的，不能索引和切片 无序
print(mult[5][1]) #10