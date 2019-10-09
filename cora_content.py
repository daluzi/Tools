# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/8 22:47
# @File     : cora_content.py
# @Software : PyCharm

import numpy as  np
import os
import scipy.io as sio
import numpy as np

file_path = "./cora/cora.content"
mat_path = "./cora/cora_content.mat"

def ReadTxtData(filePath):
	resultData = []
	gnd = []
	with open(filePath,"r") as f:
		for line in f:
			f = list(line.strip("\n").split("\t"))
			del f[0]
			resultData.append(f)
			a = f[1433]
			if a not in gnd:
				gnd.append(a)
	return resultData,gnd


r,g = ReadTxtData(file_path)
r = np.array(r)
print("r:\n",r)
print(g)

dic = {}
for i in range(len(g)):
	asd = g[i]
	dic.update({asd:i+1})
print(list(dic.keys())[0])
print(dic)

for i in range(len(r)):
	# print(r[i][1433])
	for j in range(7):
		if r[i][1433] == list(dic.keys())[j]:
			r[i][1433] = list(dic.values())[j]

print("R\n",r)
print(type(r))
print(r.shape)
r_to_int = []
for i in range(len(r)):
	w = r[i]
	r_to_int.append(list(map(lambda x:int(x), w)))
r_to_int = np.array(r_to_int)
sio.savemat(mat_path, {'content':r_to_int})
data = sio.loadmat(mat_path)
print(data['content'])