# -*- coding: utf-8 -*-
'''
@Time    : 2020/12/4 22:23
@Author  : daluzi
@File    : test.py
'''



import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.sum(axis=1))

num = 1
print("%d" % (num))
print("%2d" % (num))
print("%02d" % (num))
print("%-2d" % (num))
print("%.2d" % (num))

print("{0:<10}{1:>5}".format(12,24))