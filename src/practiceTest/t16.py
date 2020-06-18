def function7_1():
    for x in range(1,11):
        print('{:5d}{:5d}{:8d}'.format(x,x*x,x*x*x))

def function7_2():
    for x in range(1,11):
        print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
        print(repr(x*x*x).rjust(4))

def func7_3(tmp):
    print(str(tmp).zfill(5))

def fun7_4():
    table={'stred':123,'bbv':2364,'a':34578}
    for a,b in table.,():
        print('{0:10}==>{1:10d}'.format(a,b))

if __name__ == "__main__":
    function7_1()
    fun7_4()
    # function7_2()
    # func7_3('-2.3123') #-2.3123