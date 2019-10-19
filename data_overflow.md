# Python数据溢出（或出现NAN）问题

##### 【数据溢出问题】

overflow：溢出 

- overflow：上溢
- underflow：下溢 

数据溢出包括上溢和下溢。

上溢可以理解为：你想用一个int类型来保存一个非常非常大的数，而这个超出了int类型所能表示的最大的数的范围。

下溢同理：你要用double来表示一个非常非常小的数，超出它所能表示的最小数时，就会发生数据溢出错误。



##### 【如何避免Python程序下溢问题】

浮点数的下溢一般是由很多很小的数（如很多独立同分布数据的概率相乘）的连乘造成的，连乘后的数值有时候会达到负几十万个指数级。



先看看 Python 2，它有两种整数：

- 一种是短整数，也即常说的整数，用 int 表示，有个内置函数 int()。其大小有限，可通过`sys.maxint()` 查看（取决于平台是 32 位还是 64 位）
- 一种是长整数，即大小无限的整数，用 long 表示，有个内置函数 long()。写法上是在数字后面加大写字母 L 或小写的 l，如 1000L

当一个整数超出短整数范围时，它会自动采用长整数表示。举例，打印 `2**100` ，结果会在末尾加字母 L 表示它是长整数。

但是到了 Python 3，情况就不同了：它仅有一种内置的整数，表示为 int，形式上是 Python 2 的短整数，但实际上它能表示的范围无限，行为上更像是长整数。无论多大的数，结尾都不需要字母 L 来作区分。

也就是说，Python 3 整合了两种整数表示法，用户不再需要自行区分，全交给底层按需处理。

理论上，Python 3 中的整数没有上限（只要不超出内存空间）。这就解释了前文中直接打印两数相乘，为什么结果会正确了。

PEP-237（Unifying Long Integers and Integers）中对这个转变作了说明。它解释这样做的 目的：

> 这会给新的 Python 程序员（无论他们是否是编程新手）减少一项上手前要学的功课。

Python 在语言运用层屏蔽了很多琐碎的活，比如内存分配，所以，我们在使用字符串、列表或字典等对象时，根本不用操心。整数类型的转变，也是出于这样的便利目的。（坏处是牺牲了一些效率，在此就不谈了）

回到前面的第二个话题：Numpy 中整数的上限是多少？

由于它是 C 语言实现，在整数表示上，用的是 C 语言的规则，也就是会区分整数和长整数。

有一种方式可查看：

```
import numpy as np

a = np.arange(2)
type(a[0])

# 结果：numpy.int32
复制代码
```

也就是说它默认的整数 int 是 32 位，表示范围在 -2147483648 ~ 2147483647。



Numpy 支持的数据类型要比 Python 的多，相互间的区分界限很多样：

![numpy_dtype](https://github.com/daluzi/Tools/blob/master/pho/numpy_dtype.png)



要解决整数溢出问题，可以通过指定 dtype 的方式：

```
import numpy as np

q = [100000]
w = [500000]

# 一个溢出的例子：
a = np.array(q)
b = np.array(w)
print(a*b)  # 产生溢出，结果是个奇怪的数值

# 一个解决的例子：
c = np.array(q, dtype='int64')
d = np.array(w, dtype='int64')
print(c*d) # 没有溢出：[50000000000]
```
