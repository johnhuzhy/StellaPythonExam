
#虽然是import * 但是并没有都引用进来。要在__init__.py文件里定义__all__=['','']放入了才可以引用进来
#在用的时候，一定是文件名，像类名.变量的意思，不能直接用变量，或者是t.learning
from t import *
print(c6.learning)
print(c7.my_name)
#impot里必须用t.
print(t.sys.path)

