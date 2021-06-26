

# python-learn



> 该文档仅用于个人学习

# 1、项目结构

当我们刚接收到一个公司项目时，第一步要做的必然是设计项目框架，一个好的项目框架应该具有 可读性 + 可维护性的特点。

以下根据个人观点尝试设计一份项目框架

由于个人比较喜欢django的项目框架，故尝试见解之并试用一段时间。

```
|-- project				  #  项目文件总目录
    |-- main.py            #  代码程序入口
    |-- setup.py            #  安装、部署、打包的脚本,能快速便捷的在一台新机器上将环境装好、代码部署好和将程序运行起来
    |-- settings            #  配置文件目录
        |-- setting-dev.py          #  开发环境的配置文件
        |-- setting-master.py        #  生产环境配置文件
        |-- setting-test.py          #  测试环境配置文件
    |-- src                #  代码主目录
        |-- apps           #  小工程主目录
            |-- app1        
                |-- urls.py   # 路由设置  
                |-- views.py  # 业务逻辑处理部分  
                |-- tests.py  # 对于小模块的测试单元   
                |-- models.py  # 用于数据库处理的一些业务逻辑
            |-- app2      # 建议 针对多个小工程建立多个app  每个小工程的业务逻辑足够简单  
            .
            .
            .
        |-- static           #  静态内容
            |-- css 
            |-- js
            |-- images
            |-- ui        # 除了上面的几个用于网站开发 同时也可能用于开发桌面应用 故添加此目录
    |-- test                #  测试单元  针对整个项目的
        |-- test.py        
    |-- scripts                #  一些脚本文件 可以为任意格式的脚本
        |-- scripts1.py        
        |-- scripts2.sh   
    |-- docs                #  用于存放一下文档
    |-- requirements.txt    #  方便开发者维护软件的包依赖。将开发过程中新增的包添加进这个列表中，避免在setup.py安装依赖时漏掉软件包。
    |-- requirements_dev.txt ,比requirements.txt多的是单元测试库
       
```



# 2、项目规范

## 一、setup.py与requirements.txt的使用

​     专业的python项目setup.py是必须的因为它包含了版本，包依赖信息，PyPi需要的项目描述，你的名字和联系信息，以及其它一些信息。它允许以编程的方式搜索安装包，提供元数据和指令说明让工具如何做。

###   最小例子

参考 https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/

```python
from  setuptools  import  setup ,  find_packages 

setup ( 
    name = 'example' ,    # 包的名称 最好与所在文件夹名称一致
    version = '0.1.0' ,   # 包的版本
    packages = find_packages ( include = [ 'exampleproject' ,  'exampleproject.*' ]),  # 要包含的包
    # 您可以指定不带版本的要求 ( PyYAML)、固定版本 ( pandas==0.23.3)、指定最低版本 ( 'numpy>=1.14.5) 或设置版本范围 ( matplotlib>=2.2.0,																				<3.0.0)。这些要求将pip在您安装软件包时自动安装。
    install_requires = [  
        'PyYAML' , 
        'pandas==0.23.3' , 
        'numpy>=1.14.5' , 
        'matplotlib>=2.2.0, , 
        'jupyter' 
    ], 
    # 在特殊情况下才需要的依赖项，例如测试环境需要而生产环境不需要的  
    # 当我们指定了我们需要的可选的interactive依赖关系（pip install example[interactive]或pip install -e .[interactive])
    extras_require = { 
        'interactive' :  [ 'matplotlib>=2.2.0',  'jupyter' ], 
    },   
    # 将包的功能公开给命令行的最佳方法,使用命令my-command在命令行中，这将反过来执行main函数内exampleproject/example.py。
    entry_points = { 
        'console_scripts' :  [ 'my-command=exampleproject.example:main' ] 
    } ,
  
)
```

# 3、  单元测试模块

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。是开发项目中必不可少的一部分

### 关于断言

| Method                                                       | Checks that                                                  | New in |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----- |
| [`assertEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertEqual) | `a == b`                                                     |        |
| [`assertNotEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotEqual) | `a != b`                                                     |        |
| [`assertTrue(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertTrue) | `bool(x) is True`                                            |        |
| [`assertFalse(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertFalse) | `bool(x) is False`                                           |        |
| [`assertIs(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIs) | `a is b`                                                     | 3.1    |
| [`assertIsNot(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIsNot) | `a is not b`                                                 | 3.1    |
| [`assertIsNone(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIsNone) | `x is None`                                                  | 3.1    |
| [`assertIsNotNone(x)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIsNotNone) | `x is not None`                                              | 3.1    |
| [`assertIn(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIn) | `a in b`                                                     | 3.1    |
| [`assertNotIn(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotIn) | `a not in b`                                                 | 3.1    |
| [`assertIsInstance(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertIsInstance) | `isinstance(a, b)`                                           | 3.2    |
| [`assertNotIsInstance(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotIsInstance) | `not isinstance(a, b)`                                       | 3.2    |
|                                                              |                                                              |        |
| [`assertAlmostEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertAlmostEqual) | `round(a-b, 7) == 0`                                         |        |
| [`assertNotAlmostEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual) | `round(a-b, 7) != 0`                                         |        |
| [`assertGreater(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertGreater) | `a > b`                                                      | 3.1    |
| [`assertGreaterEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertGreaterEqual) | `a >= b`                                                     | 3.1    |
| [`assertLess(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertLess) | `a < b`                                                      | 3.1    |
| [`assertLessEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertLessEqual) | `a <= b`                                                     | 3.1    |
| [`assertRegex(s, r)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertRegex) | `r.search(s)`                                                | 3.1    |
| [`assertNotRegex(s, r)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertNotRegex) | `not r.search(s)`                                            | 3.2    |
| [`assertCountEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertCountEqual) | *a* and *b* have the same elements in the same number, regardless of their order. | 3.2    |
|                                                              |                                                              |        |
| [`assertMultiLineEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual) | strings                                                      | 3.1    |
| [`assertSequenceEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertSequenceEqual) | sequences                                                    | 3.1    |
| [`assertListEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertListEqual) | lists                                                        | 3.1    |
| [`assertTupleEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertTupleEqual) | tuples                                                       | 3.1    |
| [`assertSetEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertSetEqual) | sets or frozensets                                           | 3.1    |
| [`assertDictEqual(a, b)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertDictEqual) | dicts                                                        | 3.1    |



| [`assertRaises(exc, fun, *args, **kwds)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertRaises) | `fun(*args, **kwds)` raises *exc*                            |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| [`assertRaisesRegex(exc, r, fun, *args, **kwds)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertRaisesRegex) | `fun(*args, **kwds)` raises *exc* and the message matches regex *r* | 3.1  |
| [`assertWarns(warn, fun, *args, **kwds)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertWarns) | `fun(*args, **kwds)` raises *warn*                           | 3.2  |
| [`assertWarnsRegex(warn, r, fun, *args, **kwds)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertWarnsRegex) | `fun(*args, **kwds)` raises *warn* and the message matches regex *r* | 3.2  |
| [`assertLogs(logger, level)`](https://docs.python.org/zh-cn/3/library/unittest.html#unittest.TestCase.assertLogs) | The `with` block logs on *logger* with minimum *level*       | 3.4  |

