# coding=UTF-8
import sys
import numpy

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