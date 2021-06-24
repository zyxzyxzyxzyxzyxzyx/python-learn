from setuptools import setup, find_packages

setup(
    name='how_to_use_setup',  # 包的名称 最好与所在文件夹名称一致
    version='0.1.0',  # 包的版本
    packages=find_packages(include=['how_to_use_setup', 'how_to_use_setup.*']),  # 要包含的包 您可以指定不带版本的要求 ( PyYAML)、固定版本 (
    # pandas==0.23.3)、指定最低版本 ( 'numpy>=1.14.5) 或设置版本范围 ( matplotlib>=2.2.0)
    # <3.0.0)。这些要求将pip在您安装软件包时自动安装。
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'jupyter'
    ],
    # 在特殊情况下才需要的依赖项，例如测试环境需要而生产环境不需要的
    # 当我们指定了我们需要的可选的interactive依赖关系（pip install example[interactive]或pip install -e .[interactive])
    extras_require={
        'interactive': ['matplotlib>=2.2.0', 'jupyter'],
    },
    # 将包的功能公开给命令行的最佳方法,使用命令my-command在命令行中，这将反过来执行main函数内exampleproject/example.py。
    entry_points={
        'console_scripts': ['my-command=how_to_use_setup:main']
    },

)
