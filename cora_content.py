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
	art = []
	with open(filePath,"r") as f:
		for line in f:
			f = list(line.strip("\n").split("\t"))
			art.append(f[0])
			# del f[0]
			resultData.append(f)
			a = f[1434]
			if a not in gnd:
				gnd.append(a)
	return resultData,gnd,art


r,g,art = ReadTxtData(file_path)
r = np.array(r)
print("r:\n",r)
print("gnd:\n",g)
# art = list(map(lambda x:int(x), art))
# art = sorted(art,reverse=False)

art = np.array(list(map(lambda x:int(x), art)))
art = sorted(art,reverse=False)
print("art:\n",art)
# art = np.array(art)
xiabiao = list(enumerate(art))
print(xiabiao[0][1])

dic = {}
for i in range(len(g)):
	asd = g[i]
	dic.update({asd:i+1})
# print(list(dic.keys())[0])
# print(dic)

for i in range(len(r)):
	# print(r[i][1433])
	for j in range(7):
		if r[i][1434] == list(dic.keys())[j]:
			r[i][1434] = list(dic.values())[j]

# print("R\n",r)
# print(type(r))
# print(r.shape)
r_to_int = []
for i in range(len(r)):
	w = r[i]
	r_to_int.append(list(map(lambda x:int(x), w)))
r_to_int = np.array(r_to_int)
r_to_int = r_to_int[np.lexsort(r_to_int[:,::-1].T)]
print("asd",r_to_int)
r_to_int = r_to_int.tolist()
for i in range(len(r_to_int)):
	r_to_int[i].pop(0)
sio.savemat(mat_path, {'X':r_to_int})
data = sio.loadmat(mat_path)
print("cora_content.mat:\n",data['X'])


'''
	cora_cites
'''

cites_filepath = "./cora/cora.cites"
cites_mat_path = "./cora/cora_cites.mat"
coraCites = np.zeros((2708,2708))
print("coraSets:\n",coraCites[0][0])

def ReadCitesData(filePath):
	resultData = []
	with open(filePath,"r") as f:
		for line in f:
			f = list(line.strip("\n").split("\t"))
			resultData.append(f)
	return resultData

cr = ReadCitesData(cites_filepath)
cr = np.array(cr)
# print("cr:\n",cr)

cr_to_int = []
for i in range(len(cr)):
	w = cr[i]
	cr_to_int.append(list(map(lambda x:int(x), w)))
cr_to_int = np.array(cr_to_int)
cr_to_int = cr_to_int[np.lexsort(cr_to_int.T)]
print("cr:\n",cr_to_int)
# cr_to_int = np.array(cr_to_int)
print(len(cr_to_int))
for i in range(len(cr_to_int)):
	for j in range(len(xiabiao)):
		if cr_to_int[i][1] == xiabiao[j][1]:
			f1 = xiabiao[j][0]
			# print(cr_to_int[i][0])
			for k in range(len(xiabiao)):
				if cr_to_int[i][0] == xiabiao[k][1]:
					f2 = xiabiao[k][0]
					coraCites[f2][f1] = 1
					coraCites[f1][f2] = 1

print(coraCites)
sio.savemat(cites_mat_path, {'content':coraCites})