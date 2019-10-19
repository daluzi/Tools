# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/10 15:26
# @File     : metrices.py
# @Software : PyCharm
import numpy as np
import math

'''
	VSS
'''
def VectorSpaceSimilarity(R,I,si,sf):
	'''
	VSS
	:param R: m*n rating matrix,m users,n items
	:param I: m*n demension, according to R: if user ui rated item vj,then Iij is equal to 1. and equal to 0 otherwise
	:param si: user i
	:param sf: user f
	:return: VSS
	'''
	sumRijRfj = 0
	sumRij = 0
	sumRfj = 0
	Rows,Columns = np.shape(R)
	for i in range(Columns):
		if I[si][i] == 1 and I[sf][i] == 1:
			sumRijRfj = sumRijRfj + R[si][i] * R[sf][i]
			sumRij = sumRij + np.square(R[si][i])
			sumRfj = sumRfj + np.square(R[sf][i])
	sumRij += 0.0001
	sumRfj += 0.0001
	simIF = sumRijRfj / (np.sqrt(sumRij) * np.sqrt(sumRfj))
	# print("sumRijRfj:\t",sumRijRfj)
	# print("sumRfj:\t",sumRfj)
	# print("sumRij:\t",sumRij)
	# print(simIF)
	return simIF

'''
	PCC
'''
def PearsonCorrelationCoefficient(R,I,si,sf):
	'''
	PCC
	:param R: m*n rating matrix,m users,n items
	:param I: m*n demension, according to R: if user ui rated item vj,then Iij is equal to 1. and equal to 0 otherwise
	:param si: user i
	:param sf: user f
	:return: VSS
	'''
	sumRijRfj = 0
	sumRij = 0
	sumRfj = 0
	Rows, Columns = np.shape(R)
	avgRij = np.sum(R[si]) / Columns
	avgRfj = np.sum(R[sf]) / Columns
	for i in range(Columns):
		if I[si][i] == 1 and I[sf][i] == 1:
			sumRijRfj += (R[si][i] - avgRij) * (R[sf][i] - avgRfj)
			sumRij += np.square(R[si][i] - avgRij)
			sumRfj += np.square(R[sf][i] - avgRfj)
	simIF = sumRijRfj / (np.sqrt(sumRij) * np.sqrt(sumRfj))
	return simIF


R = [[1,2,3,4,5],[2,0,3,0,5],[2,3,0,0,0]]
I = [[1,0,1,0,0],[1,1,0,0,1],[1,1,1,1,1]]
VectorSpaceSimilarity(R, I, 1,2)