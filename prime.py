# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/11/13 16:10
# @File     : prime.py
# @Software : PyCharm

import math
def prime(n):
	for i in range(2,round(math.sqrt(n)+1)):
		if (n % i) == 0:
			print("%d不是素数"%(n))
			break
	else:
		print("%d是素数"%(n))
m = int(input("请输入一个数:"))
for i in range(1,m):
	prime(i)