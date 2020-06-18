#绝对路径导入时，要从顶级包开始，main和要导入的m1都是在src下，所以m1的顶级包是package1
#import package1.m1

#相对导入  .同级目录 ..上一级目录  
# from .package2.m2 import a

#在入口文件里不要用相对路径*（自己执行那个文件

import package2.m2



