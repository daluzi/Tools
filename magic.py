# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/24 15:28
@Author  : daluzi
@File    : magic.py
'''


'''
    连接多个列表
'''
a = [1,2]
b = [3,4]
c = [5,6]
print(a+b+c)
print(sum((a,b,c), []))


'''
    当一个or表达式中所有值都为真，Python会选择第一个值
    当一个and表达式中所有值都为真，Python会选择第二个值
'''
print((2 or 3) * (5 and 7)) #14


'''
    在Python3.6+中字典已经是有序的
'''
mydict = {str(i): i for i in range(5)}
print(mydict)


'''
    为了避免整数频繁申请和销毁内存空间，Python定义了一个小整数池[-5,256]，这些整数对象是提前建立好的，不会被垃圾回收。
    在pycharm中运行python程序时，pycharm出于对性能的考虑，会扩大小整数池的范围，其他的字符串等不可变类型也都包含在内一便采用相同的方式处理了，我们只需要记住这是一种优化机制，至于范围到底多大，无需细究。
'''
a = -6
b = -6
print(a is b) #Pycharm上运行得到的结果是True，终端上运行得到的结果是False。
a = 256
b = 256
print(a is b) #Pycharm和终端上运行的结果都是True。
a = 257; b = 257
print(a is b) #Pycharm和终端上运行的结果都是True，因为当在同一行里，同时给两个变量赋同一值时，解释器知道这个对象已经生成，那么它就会引用到同一个对象。如果分成两行的话，解释器并不知道这个对象已经存在了，就会重新申请内存存放这个对象。


'''
    神奇的intern机制
'''
# intern（字符串驻留）技术，就是同样的字符串对象仅仅会保存一份，放在一个字符串储蓄池中，是共用的，不可变
# 如果字符串中有空格，默认不启用intern机制
# 如果一个字符串长度超过20个字符，不启动intern机制



from distutils.sysconfig import get_python_lib
print(get_python_lib())