# coding=UTF-8
import sys

import numpy
from numpy import *
import sys

def ReadTxtData(filePath):
	resultData = []
	with open(filePath,"r") as f:
		for line in f:
			resultData.append(list(line.strip("\n").split("::")))
	print(len(resultData))
	print(resultData)
	return resultData

def ReadTxtData_np(filename):
	dataSet = numpy.loadtxt(filename)
	return dataSet

if __name__ == "__main__":
	a = [[1,20],[2,32]]
	x = []
	for i,j in a:
		print(i,j)
		x.append(j)
	print(x)
	b = '6040::2019::5::956703977'
	print(b.strip("\n").split("::"))
	print(list(b.strip("\n").split("::")[i] for i in range(3)))

	r = 1
	newX = [[a[i][j] + r for j in range(len(a[i]))] for i in range(len(a))]
	print(newX)

	print(sys.getsizeof(1))#28
	print(sys.getsizeof([]))#64
	print(sys.getsizeof(()))#48
	print(sys.getsizeof({}))#240
	print(sys.getsizeof(True))#28