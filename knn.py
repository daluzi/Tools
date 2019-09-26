# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/9/26 13:27
# @File     : knn.py
# @Software : PyCharm

import numpy as np

def myKNN(S, k, sigma=1.0):
	N = len(S)  # 输出的是矩阵的行数
	A = np.zeros((N, N))

	for i in range(N):
		dist_with_index = zip(S[i], range(N))
		# print(list(dist_with_index))
		print(dist_with_index)
		dist_with_index = sorted(dist_with_index, key=lambda x: x[0], reverse=True)
		print(dist_with_index)
		neighbours_id = [dist_with_index[m][1] for m in range(k)]  # xi's k nearest neighbours
		# print("neigh",neighbours_id)
		for j in neighbours_id:  # xj is xi's neighbour
			# print(j)
			A[i][j] = 1
			A[j][i] = A[i][j]  # mutually
	# print(A[i])
	m = np.shape(A)[0]
	print(m)
	for i in range(m):
		for j in range(m):
			if j == i:
				A[i][j] = 0
	return A

if __name__ == "__main__":
	test = [[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10],[6,7,8,9,10]]
	print(myKNN(test,5))