def function8_1():
    while True:
        try:
            x=input("数字を入れてください")
            break
        except ValueError:
            print("あちら！これは有効な数字ではありません。もう一度")

#else 是和try一起的，try里没有异常时才会走else，如果try里报错了，不会走else。finally是都会走的
def divide(x,y):
    try:
        result=x/y
        # raise KeyError
    except ZeroDivisionError:
        print("ゼロ除算")
    else:
        print("答えは",result)
    finally:
        print("finally节执行中")

if __name__ == "__main__":
    # function8_1()
    divide(2,1)
    divide(2,0)
