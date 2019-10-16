# Be_pythonic

- 使用迭代器iterator，for example：

​    　　dict的iteritems 而不是items（同itervalues，iterkeys）

​    　　使用generator，特别是在循环中可能提前break的情况

- 判断是否是同一个对象使用 is 而不是 ==

- 判断一个对象是否在一个集合中，使用set而不是list

- 利用短路求值特性，把“短路”概率过的逻辑表达式写在前面。其他的[lazy ideas](http://www.cnblogs.com/xybaby/p/6425735.html)也是可以的

- 对于大量字符串的累加，使用join操作

- 使用for else（while else）语法

- 交换两个变量的值使用： a, b = b, a