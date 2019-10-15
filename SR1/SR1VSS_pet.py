# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/10 22:24
# @File     : SR1VSS_set.py
# @Software : PyCharm

import metrices
import numpy as np
from numpy import *
import random


# 读取txt文件
def ReadTxtData(filePath):
	resultData = []
	with open(filePath, "r") as f:
		for line in f:
			resultData.append(list(line.strip("\n").split("::")))
	# print(len(resultData))
	print(resultData)
	return resultData

#处理原始数据
def ProData(dataSet):
	dataSetSecondColu = []
	for i in range(len(dataSet)):
		dataSetSecondColu.append(dataSet[i][1])
	dataSetSecondColu = list(set(list(map(lambda x: float32(x), dataSetSecondColu))))  # 字符型转为int，然后去重
	# dataSetSecondColu = dataSetSecondColu))#去重
	dataSetSecondColu.sort()  # 排序
	print(dataSetSecondColu)
	# print("下标:\n",dataSetSecondColu.index(149532))
	user_item_matrix = np.zeros((669, 10325))

	dataSet = [np.array(list(map(lambda x: float32(x), dataSet[i]))) for i in range(len(dataSet))]  # 字符数组转化为数字数组
	dataSet = np.array(dataSet)
	twiColu = dataSet[np.lexsort(dataSet.T[1, None])]  # 按照第二列即item排序

	print("twiColu:\n", twiColu)
	print(np.array(twiColu).shape)
	for i in range(len(dataSet)):
		m = int(dataSet[i][0])
		n = int(dataSetSecondColu.index(dataSet[i][1]))
		r = dataSet[i][2]
		# print(m,n,r)
		user_item_matrix[m][n] = r
	hang, lie = shape(user_item_matrix)
	print("hang", hang, lie)
	train_matrix = user_item_matrix
	test_matrix = np.zeros((hang, lie))
	line = np.argwhere(train_matrix > 0)
	line1 = int(0.2 * len(line))
	print(line1)

	for i in range(hang):
		randomResult = random.sample(range(1, lie), int(0.2 * lie))
		for j in range(len(randomResult)):
			o = randomResult[j]
			test_matrix[i][o] = train_matrix[i][o]
			train_matrix[i][o] = 0

	trc = np.array(np.argwhere(train_matrix > 0))
	print("trc:\n", trc)
	lentrc = len(trc)
	print("trc.length:\n", lentrc)
	# print("each:\n",trc[2][1])
	total = 0
	for i in range(lentrc):
		total += train_matrix[trc[i][0]][trc[i][1]]
	# print(total)
	trainR = total / lentrc
	print("trainR:\n", trainR)

	return trainR, train_matrix, test_matrix



class SR1:

	def __init__(self,filepath):
		readData = ReadTxtData(filepath)#读取文件'
		ProData(readData)
		pass



if __name__ == '__main__':
	filePath = './pets/ratings.txt'
	sr1 = SR1(filePath)