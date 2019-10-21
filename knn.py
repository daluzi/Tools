# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/9/26 13:27
# @File     : knn.py
# @Software : PyCharm

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import pdist,squareform #此也为计算相似矩阵的一个库,dist_matrix = squareform(pdist(data,metric='euclidean'))

def myKNN(S, k, sigma=1.0):
	N = len(S)  # 输出的是矩阵的行数
	A = np.zeros((N, N))

	for i in range(N):
		# print(S[i])
		dist_with_index = zip(S[i], range(N))
		# print(list(dist_with_index))
		# print(list(dist_with_index)[0])
		dist_with_index = sorted(dist_with_index, key=lambda x: x[0], reverse=True)
		# print(dist_with_index)
		# print(dist_with_index[1][1])
		neighbours_id = [dist_with_index[m][1] for m in range(k)]  # xi's k nearest neighbours
		# print("neigh",neighbours_id)
		for j in neighbours_id:  # xj is xi's neighbour
			# print(j)
			A[i][j] = 1
			# A[j][i] = A[i][j]  # mutually
	# print(A[i])
	m = np.shape(A)[0]
	# print(m)
	for i in range(m):
		for j in range(m):
			if j == i:
				A[i][j] = 0
	return A

def trainW1(v):
	similarMatrix = cosine_similarity(v)
	m = np.shape(similarMatrix)[0]
	print(m)
	for i in range(m):
		for j in range(m):
			if j == i:
				similarMatrix[i][j] = 0
	return similarMatrix
def trainW(v):
	similarMatrix = cosine_similarity(v)
	m = np.shape(similarMatrix)[0]
	# print(m)
	# for i in range(m):
	# 	for j in range(m):
	# 		if j == i:
	# 			similarMatrix[i][j] = 0
	print("asdad",similarMatrix)
	return similarMatrix

if __name__ == "__main__":
	test = [[1,2,3,4,5],[6,7,8,9,10],[16,7,8,19,10],[6,7,18,39,10],[46,27,8,9,10],[46,27,8,9,10]]
	print(np.array(test).shape)
	test1 = trainW(test)
	te = trainW(test1)
	test2 = trainW1(test)

	print("test1:\n",test1)
	print("test2:\n",test2)
	print(myKNN(test,3))
	print(myKNN(test1,3))
	print(myKNN(test2,3))

	asd = [[1,2,3,4],[2,3,4,5]]
	asd = [[asd[i][j] + 1 for j in range(len(asd[i]))] for i in range(len(asd))]#每个元素累加1
	print("asd",asd)