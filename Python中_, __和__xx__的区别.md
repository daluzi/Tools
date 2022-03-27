# Python中`_`, `__`,`__xx__`,`XX_`的区别

## “`_`”单下划线

Python中不存在真正的私有方法。为了实现类似于C++中的私有方法，可以在类的方法或属性前加一个“`_`”单下划线，意味着<font color='red'>该方法或属性不应该去调用</font>，它不属于API。



## “`__`”双下划线

它不是用来标识一个方法或属性是私有的，真正作用是<font color='red'>用来避免子类覆盖其内容。</font>

举栗子：

```python
class A(object):
    def __method(self):
        print("I'm a method in A" )
    def method(self):
        self.__method()
a = A()
a.method()

class B(A):
    def __method(self):
        print( "I'm a method in B" )
b = B() 
b.method()
```

结果：

```python
I'm a method in A
I'm a method in A
```

在Python中如是做的？很简单，它只是把方法重命名了.



## “`__XX__`”双下划线

```python
当你看到"__this__"的时，就知道不要调用它。为什么？因为它的意思是它是用于Python调用的，如下：
>>> name = "igor" 
>>> name.__len__() 4 
>>> len(name) 4 
>>> number = 10 
>>> number.__add__(20) 30 
>>> number + 20 30
```

`__XX__`经常是操作符或本地函数调用的magic methods。在上面的例子中，提供了一种重写类的操作符的功能。

在特殊的情况下，它只是python调用的hook。例如，`__init__()`函数是当对象被创建初始化时调用的;`__new__()`是用来创建实例。

```python
class CrazyNumber(object):
    def __init__(self, n): 
        self.n = n 
    def __add__(self, other): 
        return self.n - other 
    def __sub__(self, other): 
        return self.n + other 
    def __str__(self): 
        return str(self.n) 

num = CrazyNumber(10) 
print num # 10
print num + 5 # 5
print num - 20 # 30    
```



## xx_

单后置下划线，用于避免与python关键字的冲突。