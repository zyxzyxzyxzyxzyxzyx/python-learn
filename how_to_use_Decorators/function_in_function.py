"""function in function"""


# 函数内部也可以写函数 并可以返回函数

def printHello(name, c="EN"):
    def englishHi():
        return "hello! {}".format(name)

    def cnHi():
        return "你好呀! {}".format(name)

    if c == "CN":
        return cnHi
    else:
        return englishHi


a = printHello(name="吴彦祖", c="CN")
print(a)
# <function printHello.<locals>.cnHi at 0x00000157CBC341E0>  相当于a变量就是cnHi
print(a())
# 你好呀! 吴彦祖

b = printHello(name="彭于晏")
print(b)
# <function printHello.<locals>.englishHi at 0x000001EC659942F0>  相当于b变量就是englishHi
print(b())
# 你好呀! 彭于晏


"""
下面来看看关键的地方 
我们可以把函数作为一个参数传入另一个函数
"""


def add_str(func):
    print(func())
    print("你好帅啊!")


add_str(printHello(name="彭于晏"))

# 打印了什么?
# hello! 彭于晏
# 你好帅啊!

# 理解到精髓没有.....其实这就是装饰器！！ ====> 在原有的函数上新增了功能
