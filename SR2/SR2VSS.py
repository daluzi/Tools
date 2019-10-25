# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/22 10:58
# @File     : SR2VSS.py.py
# @Software : PyCharm
from sklearn.metrics.pairwise import cosine_similarity

import metrices
import numpy as np
from numpy import *
import random_test
import copy
import metrices
from sklearn.metrics import mean_squared_error #均方误差
from sklearn.metrics import mean_absolute_error #平方绝对误差
import random
import gc

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
		randomResult = random.sample(range(1, lie), int(0.1 * lie))
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
			# A[j][i] = A[i][j]  # mutually
	# print(A[i])
	m = np.shape(A)[0]
	for i in range(m):
		for j in range(m):
			if j == i:
				A[i][j] = 0
	return A


class SR2:

	def __init__(self,filepath,k):
		readData = ReadTxtData(filepath)#读取文件'
		r, train, test = ProData(readData)
		U, V = self.Update(train, k, 10, 0.001, 0.001, 0.001, 0.001)
		print("----------------------------------------------")
		print("U:\n",U)
		print("V:\n",V)
		new = np.dot(U.T, V)
		self.test = test
		self.new = new
		self.r = r
		pass

	def Update(self, R, k, r, lamb1, lamb2, aerfa, aerfa1):
		'''

		:param R: user-item matrix
		:param k: The number of iterations
		:param r: r-rank factors
		:param lamb1: used to calculate U
		:param lamb2: used to calculate V
		:param aerfa:
		:param aerfa1:
		:return:
		'''
		print("R:\n",R)
		I = copy.copy(R)
		I[I > 0] = 1

		m, n = R.shape
		U = np.array(np.random.random((r, m)),dtype='float16')
		V = np.array(np.random.random((r, n)),dtype='float16')

		#这里可以通过KNN找到user的朋友矩阵
		simiX = trainW(R)
		W = myKNN(simiX, 5)
		# print("w:",W)

		# updating formulas
		for i in range(k):
			# U
			for i_u in range(m):
				subU1 = np.zeros((r, 1),dtype='float16')
				for j_u in range(n):
					# print(np.array(U[:,i_u].T).shape, np.array(V[:,j_u]).shape)
					# print(U[:,j_u].T)
					# print(V[:,j_u])
					# print(I[i_u][j_u])
					subU1 = subU1 + (I[i_u][j_u] * (np.dot(U[:,i_u].T , V[:,j_u]) - R[i_u][j_u])) * V[:,j_u]
				subU1 = subU1 + lamb1 * U[:,i_u]

				subU2on = np.zeros((r, 1))
				Fri = np.argwhere(W[i_u] == 1)
				# print(len(Fri))
				for f in range(len(Fri)):
					# print(Fri[f][0])
					# print("i_u\t",i_u)
					# print("Fri[%d][0]\t" % f,Fri[f][0])
					# print(U[:,Fri[f][0]].shape)
					# print("asdasdd:\n",subU2on)
					subU2on = subU2on + (metrices.VectorSpaceSimilarity(R, I, i_u, Fri[f][0])) * (np.array(U[:,i_u]) - np.array(U[:,Fri[f][0]]))
				# print("subU2on:\n", subU2on)
				subU2 = aerfa * subU2on[0]
				subU = subU1 + 2 * subU2

				# print("subU1:\n",subU1)
				# print("subU2:\n",subU2)
				# print("subU:\n",subU)
				del subU1
				del subU2
				U[:,i_u] = U[:,i_u] - aerfa1 * np.array(subU[0])

			#V
			for i_v in range(n):
				subV = np.zeros((1, r))
				for j_v in range(m):
					subV = subV + (I[j_v][i_v] * (np.dot(U[:,j_v].T , V[:,i_v]) - R[j_v][i_v])) * U[:,j_v]
				subV = subV + lamb2 * V[:,i_v]
				# print("subV:\n", subV)
				V[:,i_v] = V[:,i_v] - aerfa1 * subV[0]
			print("run%d" % i)

		return U, V


if __name__ == '__main__':
	filePath = './pets/ratings.txt'
	k = 200
	sr2 = SR2(filePath, k)
	# newX = [[sr2.new[i][j] + sr2.r for j in range(len(sr2.new[i]))] for i in range(len(sr2.new))]  # 每个元素累加r
	newX = sr2.new

	xiabao = np.argwhere(sr2.test > 0)  # 获取测试集中值大于0的元素的下标
	y_true = []
	y_pred = []
	for i, j in xiabao:
		y_true.append(sr2.test[i][j])
		y_pred.append(newX[i][j])

	print("y_pred", y_pred)
	print("y_true", y_true)
	print("SR1VSS RMSE:", sqrt(mean_squared_error(y_true, y_pred)))
	print("SR1VSS MAE:", mean_absolute_error(y_true, y_pred))