import t.c9
#入口文件和普通模块内置变量的区别
print('******************************************************')
print('name:'+__name__);
print('package:'+(__package__ or '当前模块不属于任何包'));
print('doc:'+(__doc__ or '当前文档没有注释'));
print('file:'+__file__);