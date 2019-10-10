# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/10 16:07
# @File     : linalg_norm.py
# @Software : PyCharm

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:33:39 2017
@author: Administrator
"""

import numpy as np

print("###########向量范数#########")
print("向量为:", [1, 5, 6, 3, -1])
print("1范数：", np.linalg.norm([1, 5, 6, 3, -1], ord=1), "向量元素绝对值之和")
print("2范数：", np.linalg.norm([1, 5, 6, 3, -1], ord=2), "向量元素绝对值的平方和再开方")
print("无穷范数:", np.linalg.norm([1, 5, 6, 3, -1], ord=np.inf), "所有向量元素绝对值中的最大值")

print("###########矩阵范数#########")
a = np.arange(12).reshape(3, 4)
print("矩阵a为：")
print(a)
print("F范数", np.linalg.norm(a, ord='fro'), "矩阵元素绝对值的平方和再开平方")
print("1范数", np.linalg.norm(a, ord=1), "列和范数，即所有矩阵列向量绝对值之和的最大值")
print("2范数", np.linalg.norm(a, ord=2), "谱范数，即ATA矩阵的最大特征值的开平方")
print("无穷范数", np.linalg.norm(a, ord=np.inf), "行和范数，即所有矩阵行向量绝对值之和的最大值")

print("###########行列式#########")
a = np.arange(1, 17).reshape(4, -1)
print("矩阵a为")
print(a)
print("a的行列式为：", np.linalg.det(a))

print("###########逆矩阵np.linalg.inv()#########")
a = np.array([[1, -1], [1, 1]])
b = np.array([[1 / 2, 1 / 2], [-1 / 2, 1 / 2]])
print("矩阵相乘为单位矩阵E:")
print(np.dot(a, b))

print("###########伴随矩阵#########")
print(a)
det_a = np.linalg.det(a)
print("a的行列式为：", det_a)
inv_a = np.linalg.inv(a)  ####求a的逆矩阵
print("a的逆矩阵为:", inv_a)
print("a的伴随矩阵为：")
bansui = det_a * inv_a
print(bansui)
print("验证:", np.dot(bansui, a))

print("###########A与A逆行列式#########")
a = np.random.rand(5, 5)
inv_a = np.linalg.inv(a)
det_a = np.linalg.det(a)
det_inv_a = np.linalg.det(inv_a)
print(det_a * det_inv_a)

print("###########矩阵的幂matrix_power()#########")
a = np.random.rand(3, 3)
print(a)
print(np.linalg.matrix_power(a, 2))

print("###########求解AXB=C?#########")
a = np.array([[1, 2, 3], [2, 2, 1], [3, 4, 3]])
b = np.array([[2, 1], [5, 3]])
c = np.array([[1, 3], [2, 0], [3, 1]])
det_a = np.linalg.det(a)
det_b = np.linalg.det(b)
inv_a = np.linalg.inv(a)
inv_b = np.linalg.inv(b)
if det_a != 0:
	if det_b != 0:
		x = np.dot(np.dot(inv_a, c), inv_b)
		print(x)