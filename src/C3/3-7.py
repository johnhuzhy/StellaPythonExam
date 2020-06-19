#for循环 主要用来遍历循环 序列或者集合，字典

#break不会走后面的else
a=[1,2,3]

for x in a:
    if x==2:
        break
    print(x)
else:
    print('end EOF')

print("*"*56)

#continue 会走后面的else
for y in a:
    if y==2:
        continue
    print(y)   
else:
    print('end EOF') 
