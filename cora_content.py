# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/8 22:47
# @File     : cora_content.py
# @Software : PyCharm

import numpy as  np
import os
import scipy.io as scio
import numpy

file_path = "./cora/cora.content"
txt_path = "./cora/cora_content.txt"

def ReadTxtData(filePath):
	resultData = []
	gnd = []
	with open(filePath,"r") as f:
		for line in f:
			resultData.append(list(line.strip("\n").split("\t")))
			a = list(line.strip("\n").split("\t"))[1434]
			if a not in gnd:
				gnd.append(list(line.strip("\n").split("\t"))[1434])
	return resultData,gnd


r,g = ReadTxtData(file_path)
print(g)