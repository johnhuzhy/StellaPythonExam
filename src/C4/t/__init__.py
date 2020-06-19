

#如果别的都调用,把共通的import 都写在init里,批量导入，在要用的模块里导入这个模块，再用模块.调用即可
import sys
import datetime
import io

#__init__.py自动运行
a='This is __init__.py'
print(a)

#可以单独指定导入哪些类
__all__=['c6','c7']