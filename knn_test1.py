# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/9/26 14:13
# @File     : knn_test1.py
# @Software : PyCharm
from numpy import *
import operator#运算符模块

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet#距离计算使用欧式距离公式
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)#行向量相加
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()#逆序排序返回下标
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1  #此处+1是为了计数
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)#sorted得到结果，其中itemgetters是运算符模块中对元组进行逆序
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group,labels=createDataSet()
print(classify0([0,0],group,labels,3))

