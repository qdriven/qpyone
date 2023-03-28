# Package,Module,Class,Method,Function

语言如何组织: 
- package
- module
- class/field/attribute/function
- function
  
```shell
package_demos
├── __init__.py
├── module_one.py
└── what_is_package.py
```
---

## Package

- 什么是package?
> Prompt: what is python package? python的package 是什么？
> Warp AI: A Python package is a way to organize related Python modules into a single directory hierarchy. A package can contain sub-packages, modules, and even other packages. It allows for better organization and reuse of code. 
> Python的package是一种将相关的Python模块组织到单个目录层次结构中的方法。一个package可以包含子package、模块，甚至是其他的package。它可以更好地组织和重用代码。
- 目的是什么？

---

## 如何使用Package-import

- 使用**import** 关键字就可以导入package:
```python
import numpy
numpy.array([1, 2, 3])
```

- 还有一种方法: ```importlib.import_module()```

```python
import importlib
numpy = importlib.import_module('numpy')
```

---

## 什么是python的module?

简单一句话: 一个python文件就是个module.

>In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`. A module can define functions, classes, and variables, and can also include runnable code. 
> Modules allow you to organize your code into logical units, making it easier to maintain and reuse. You can import modules in other Python scripts to use their functionality.
> 在Python中，module是一个包含Python定义和语句的文件。文件名是module名称加上`.py`后缀。一个module可以定义函数、类和变量，也可以包含可运行的代码。
> Modules允许您将代码组织成逻辑单元，使其更易于维护和重用。您可以在其他Python脚本中导入modules以使用它们的功能。

## 如何使用module?

- 使用import就可以, 如何在一个package下面那么就是:
  ``` from <package> import <module> ```
- package/module,用来组织代码,进行分层，类似目录/子目录
  - ```__init__.py```: 表示是一个package
  - package目录下面所有的py文件都是一个module

```shell
package_demos
├── __init__.py
├── module_one.py
└── what_is_package.py
```
- 访问module
  - 直接通过package，如何做到？
  - 直接访问module

--- 

## 如何使用代码load module

- importlib 使用

```python
import importlib
importlib.import_module("package_demos.module_two") 
```

--- 

### 理解从哪里开始加在包

- python运行环境地址: 自动加在默认环境下的python包
- 理解sys.modules: 通过导入python下的包进行

--- 

### class/method/attribute

```python
class ModuleClass:

    def __init__(self):
        print("this is module class")
        self.a = "a"

    def module_class_method(self):
        print(self.__name__)
        print("this is module class method!")
```

---

## Slot in Class

- What's the difference?

```python
class MySlotClass:
    __slots__ = ('attr1', 'attr2')

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


class MyClass:
    # __slots__ = ('attr1', 'attr2')

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


setattr(MyClass(1, 2), "tmp", "test")
setattr(MySlotClass(1, 2), "tmp", "test")
```
---

## 一切module相关信息都可以获取

通过使用importlib和inspect,可以做到通过代码获得: 
- module
- module下面的类
- module下面的函数
- 函数的参数

---

## 代码

```python
    module_one = importlib.import_module("package_demos.what_is_package")  
    for name in dir(module_one):
        if callable(getattr(module_one, name)): 
            if isinstance(getattr(module_one, name), type):
                print(name, type(getattr(module_one, name)))
            if isinstance(getattr(module_one, name), types.FunctionType):
                print(name, type(getattr(module_one, name)))
```
