def func9_1():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        nonlocal spam
        spam="nonlocal"
    def do_global():
        global spam
        spam="global spam"
    
    spam="test spam"
    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)

if __name__ == "__main__":
    func9_1()
    print("In global scope:",spam)



