# Python中`_`, `__`,`__xx__`,`XX_`的区别



关于cls以及调用方法的理解。

python的classmethod叫做python的累方法，是只需要在普通方法上加上@classmethod这样一个装饰器就可以。

普通方法

```javascript
def hello(self):
    pass
```

类方法

```javascript
@classmethod
def hello(cls):
    pass
```

如上代码，这就是一个最简单的类方法，这时候可以对比一下两个方法有什么不同？

除了多了一个classmethod装饰器，其实还有括号里面的参数形式发生类变化，由self变成了cls，虽然我们之前说过（）里面的参数随便叫什么都可以，self只不过是我们约定俗成的一种写法，但是在这里，从self变成了cls并不是形式上的变化，而是根本上的变化。

什么这么说呢？

self所代表的其实是对象的指针，它可以指向任意一个对象。在实例化对象的时候self就会变成对象实例。

**cls所代表的东西代表的其实是一个类本身，它可以用来调用类自己的属性和类自己的方法。**

下面可以看一个例子：

```javascript
class Hello():
    a = 1
    def h1(self):
        print ('hello 1111')

    @classmethod
    def h2(cls):
        print ('hello 22222')
```

现在我们定义了一个Hello类，在Hello类里面有h1，h2两个方法，其中h2是类方法，现在cls表演的时刻到了！

如果我想在h2里面获得类里面的a属性，我可以直接去访问吗？

![img](https://ask.qcloudimg.com/http-save/yehe-2056989/tmzgbwwm2j.png?imageView2/2/w/1620)

运行结果：

![img](https://ask.qcloudimg.com/http-save/yehe-2056989/hhajn6s2uz.png?imageView2/2/w/1620)

答案是不行的，那怎么办呢？答案是使用cls去获取a这个属性啦

```javascript
@classmethod
def h2(cls):
    print ('hello 22222')
    print (cls.a)
```

结果：

![img](https://ask.qcloudimg.com/http-save/yehe-2056989/4z02wijd62.png?imageView2/2/w/1620)

可以正常访问到属性，这点其实和self是一样的，普通方法访问类中的属性的时候也是借助于self来访问的。

下面接着看，如果我需要在h2里面调用h1方法呢？

直接写h1？

估计大家都猜到了，不行，

那就用cls

```javascript
@classmethod
def h2(cls):
    print ('hello 22222')
    print (cls.a)
    cls.h1()
```

这样写，我们来看一下结果

![img](https://ask.qcloudimg.com/http-save/yehe-2056989/kgt6wtkek0.png?imageView2/2/w/1620)

很明显是有问题的。回到一开始看看，一开始的问题cls后面为啥有括号？？把括号加上去试试。

```javascript
@classmethod
def h2(cls):
    print ('hello 22222')
    print (cls.a)
    cls().h1()
```

运行一下：

![img](https://ask.qcloudimg.com/http-save/yehe-2056989/ew9gtddvbb.png?imageView2/2/w/1620)

运行没有问题，可以调用。那为什么会这样呢？

cls其实在这个里面代表的就是一个类本身，可以就把cls()看作是Hello这个类，那调用方法直接点那个方法不就可以了吗？所以，cls（）这个东西其实就是这个类，但是现在的调用和我们一开始的调用不一样啊？

在一开始的图片中cls（）里面是有参数的呀，我们这个没有参数，那个有参数的是怎么回事呢？这些参数其实就是在构造方法中传入的参数！

```javascript
class Hello():

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def h1(self):
        print ('hello 1111')

    @classmethod
    def h2(cls):
        print ('hello 22222')
        cls(1, 2).h1()

Hello.h2()
```

所以，cls这个参数表示自身类，它的作用有：调用类的属性，类的方法，实例化对象等。最后再说一下：类方法可以同时被对象和类本身调用！

对于刚刚的Hello类

```javascript
hi = Hello(3,2)
# 对象调用
hi.h2()

# 类直接调用
Hello.h2()
```



<b>ref</b>

https://www.cnblogs.com/king-lps/p/12597680.html