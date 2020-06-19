from p2 import p2
p1=1
print(p2)

#包和模块是不会被重复导入的

#不能循环导入 p1里import p2 ,p2 里import p1  报错 ；去掉p2里的引用OK

#也不能间接循环引用， p1里import p2 ,p2 里import p3， p3里import p4 ,p4 里import p1 报错；去掉p4里的引用OK

#模块代码没有问题时，要检查引用对不对

#入口文件，一个应用程序一个入口文件