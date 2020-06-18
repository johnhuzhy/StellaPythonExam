# *代表传入是元组参数   **代表传入是字典参数
#可变长的引数放在最后，先写固定参数
#参数顺序 固定参数 ，可变参数，关键字参数(name='stella')
def cheseshop(kind,*arguments,**keywords):
    print("--Do you have any",kind,"?")
    print("--I'm sorry,we're all out of",kind)
    for arg in arguments:
        print(arg)
    print('*'*40)
    keys=sorted(keywords.keys())
    for kw in keys:
        print(kw,":",keywords[kw])


cheseshop("Limburger","it's very runny,sir.","it's really very,VERY runny,sir.",
shopkeeper="Michael Palin",client="John Cleese",sketch="Cheese shop Skeytch")

print('#'*40)
#定义元组时不加括号也是元组，list ，集合，不能去括号
t = 1,2,3,'a',"bf"
print(type(t))

print('#'*40)
s = "apple","orange",'banana'
print(type(s))
w = ["apple","orange",'banana']
print(type(w))
e = {"apple","orange",'banana'}
print(type(e))
r = ("apple","orange",'banana')
print(type(r))

print('#'*40)
x = {'shopkeeper':"Michael Palin",'client':"John Cleese",'sketch':"Cheese shop Skeytch"}
print(type(x))
#另一种定义字典的写法
y = dict(name='stella', age=26, phone='123456', sex='female')
print(type(y))