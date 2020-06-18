import os #操作操作系统和函数相关
import shutil#ファイルやディレクトリの管理
import glob #ファイルのワイルドカード　wildcard 通配符
import sys #コマンドライン引数　引数はｓｙｓモジュールのargv属性にリスト格納されている
import re #文字列パターンマッチング　正规表现
import math 

print(os.getcwd())#今いるディレクトリを返す
#os.chdir('/ss/mytest') #カレントディレクトリ変更
shutil.copyfile('e:/MyPython/StellaPythonExam/src/practiceTest/t18.py','t20.py') #copy
glob.glob('*.py')
print(sys.argv)


