<h1>super()</h1>

<b>一、单继承</b>

在单继承时，`super()`避免了基类的显式调用。

```python
class Base(object):
    def __init__(self):
        print 'Create Base'

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print 'Create A'

A()

# 测试结果
Create Base
Create A
```

```python
class Base(object):
    def __init__(self):
        print 'Create Base'

class A(Base):
    def __init__(self):
        super(A, self).__init__()
        # super().__init()  python3
        print 'Create A'

A()

# 测试结果
Create Base
Create A
```



<b>二、多继承</b>

在单继承时，`super`获取的类刚好是父类，但多继承时，`super`获取的是继承顺序中的下一个类。

```undefined
  Base
  /  \
 /    \
A      B
 \    /
  \  /
   C
```

```python
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"

class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"

class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"

class C(A, B):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"

C()

# 测试结果
enter C
enter A
enter B
enter Base
leave Base
leave B
leave A
leave C
```

```python
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"

class A(Base):
    def __init__(self):
        print "enter A"
        Base().__init__()
        print "leave A"

class B(Base):
    def __init__(self):
        print "enter B"
        Base().__init__()
        print "leave B"

class C(A, B):
    def __init__(self):
        print "enter C"
        A().__init__()
        B().__init__()
        print "leave C"

C()

# 测试结果
enter C
enter A
enter Base
leave Base
enter Base
leave Base
leave A
enter A
enter Base
leave Base
enter Base
leave Base
leave A
enter B
enter Base
leave Base
enter Base
leave Base
leave B
enter B
enter Base
leave Base
enter Base
leave Base
leave B
leave C
```

从上面可以看到如果不使用`super`，会导致基类被多次调用，开销非常大。

对于定义的类，在Python中会创建一个MRO(Method Resolution Order)列表，它代表了类继承的顺序。查看MRO列表

```ruby
class Base(object):
    def __init__(self):
        print "Create Base"

class A(Base):
    def __init__(self):
        super(A, self).__init__()
        print "Create A"

class B(Base):
    def __init__(self):
        super(B, self).__init__()
        print "Create B"

class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print "Create C"

print C.mro()

# 测试结果

[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <type 'object'>]
```

MRO的查找顺序是按广度优先来的(基类继承object，Python 2.3之后)。