# coding=UTF-8
import sys

def ReadTxtData(filePath):
	resultData = []
	with open(filePath,"r") as f:
		for line in f:
			resultData.append(list(line.strip("\n").split("::")))
	print(len(resultData))
	print(resultData)
	retrun resultData