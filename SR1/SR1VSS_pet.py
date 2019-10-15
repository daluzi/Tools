# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/10 22:24
# @File     : SR1VSS_set.py
# @Software : PyCharm
from sklearn.metrics.pairwise import cosine_similarity

import metrices
import numpy as np
from numpy import *
import random
import copy
import metrices


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
	user_item_matrix = np.zeros((1624, 1672))

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

	return trainR, train_matrix, test_matrix #r没什么用处

# 相似矩阵
def trainW(v):
	similarMatrix = cosine_similarity(v)
	m = np.shape(similarMatrix)[0]
	for i in range(m):
		for j in range(m):
			if j == i:
				similarMatrix[i][j] = 0
	return similarMatrix

# KNN
def myKNN(S, k):
	N = len(S)  # 输出的是矩阵的行数
	A = np.zeros((N, N))

	for i in range(N):
		dist_with_index = zip(S[i], range(N))
		dist_with_index = sorted(dist_with_index, key=lambda x: x[0], reverse=True)
		# print(dist_with_index)
		neighbours_id = [dist_with_index[m][1] for m in range(k)]  # xi's k nearest neighbours
		# print("neigh",neighbours_id)
		for j in neighbours_id:  # xj is xi's neighbour
			# print(j)
			A[i][j] = 1
			A[j][i] = A[i][j]  # mutually
	# print(A[i])
	m = np.shape(A)[0]
	for i in range(m):
		for j in range(m):
			if j == i:
				A[i][j] = 0
	return A


class SR1:

	def __init__(self,filepath,k):
		readData = ReadTxtData(filepath)#读取文件'
		r, train, test = ProData(readData)
		U, V = self.Update(train, k, 0)
		pass

	def Update(self, R, k, r):
		XW = copy.copy(R)
		XW[XW > 0] = 1

		m, n = R.shape
		U = np.array(np.random.random((10, m)))
		V = np.array(np.random.random((10, n)))

		#这里可以通过KNN找到user的朋友矩阵
		simiX = trainW(R)
		W = myKNN(simiX, 5)

		# updating formulas
		for i in range(k):
			# U
			for i_u in range(m):
				for j_u in range(n):
					U[i_u] = 

		return U, V


if __name__ == '__main__':
	filePath = './pets/ratings.txt'
	k = 10
	sr1 = SR1(filePath, k)