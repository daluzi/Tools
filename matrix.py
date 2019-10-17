# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/17 22:09
# @File     : matrix.py
# @Software : PyCharm

import numpy as np

# 数乘列表
a = 2
b = [1,2]
print(a * b)#[1, 2, 1, 2]。数乘列表就是列表元素重复n次
# 但如果列表里面的元素是引用类型，比如再嵌套一个列表
list1 = [[1,2]]
list2 = list1 * 2
print(list2)#[[1, 2], [1, 2]]
list2[0][0] = 5
print(list2)#[[5, 2], [5, 2]]  (说明list2[0]和list2[1]拥有同样的地址，也就是说数乘一个列表的时候，在引用类型的重复上面，是将地址重复了一个)
print(list1)#[[5, 2]]


# 数乘矩阵
a = 2
c = np.array([[1],[2]])
print(c.T)
print(np.transpose(c))
print(a * c)

# 矩阵相加
a = np.array([[1,2],[1,2]])
b = np.array([[2,1],[2,1]])
print(a + b)