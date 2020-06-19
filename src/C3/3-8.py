#这个break结束的是第二层循环，第一层循环还会去执行1，2，3
#else语句是和第一层for搭配的，所以会出力else里的内容
b=[['apple','orange','banana','grape'],(1,2,3)]
for y in b:
  for z in y:
    if z=='orange':
       break
    print(z)
else:
  print('fruit is gone') 

