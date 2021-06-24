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

