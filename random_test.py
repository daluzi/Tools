# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/17 12:55
# @File     : random_test.py
# @Software : PyCharm

import numpy as np
import random
lie = 10
randomResult = random.sample(range(1, lie), int(0.2 * lie))
print(randomResult)

np.random.seed(2019)
nd = np.random.random([10])
print(nd)
print(nd[3])
print(nd[3:6])
print(nd[1:6:2])
#倒序
print(nd[::-2])
nd1 = np.arange(25).reshape([5,5])
print(nd1[1:3,1:3])
print(nd1[(nd1>3)&(nd1<10)])
print(nd1[[1,2]])
print(nd1[1:3,:])
print(nd1[:,1:3])

a = 1000
while a > 0:
	for i in range(5):
		if i == 2:
			break
		print(i)
	a = a -1