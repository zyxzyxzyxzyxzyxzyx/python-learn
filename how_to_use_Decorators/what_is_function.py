"""what is function"""


def printHello(name="吴彦祖"):
    print("hello! {}".format(name))


printHello()
# 打印结果： hello! 吴彦祖

# python可以将函数赋值给一个变量,如:
myFunc = printHello
myFunc(name='彭于晏')
# 打印结果：hello! 彭于晏

# 若我们删除 printHello 会对myFunc 有影响吗,一起来看看
del printHello

myFunc()
# 打印结果：hello! 彭于晏
# 看来对myFunc变量来说并没有什么影响

printHello()
# 这样呢? 明显是不可行的,因为已经删除了printHello变量

"""请阅读 function_in_function"""
