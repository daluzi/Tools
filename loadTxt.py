# coding=UTF-8
import sys

import numpy
from numpy import *

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