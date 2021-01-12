# -*- coding: utf-8 -*-
'''
@Time    : 2020/12/24 10:42
@Author  : daluzi
@File    : NMF.py
'''

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

from numpy.random import RandomState
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

#图像展示的排列情况
n_row, n_col = 2, 3
#设置提取特征的数目为6
n_components = n_row * n_col
#人脸数据图片大小
image_shape = (64, 64)
# Load faces data，并打乱顺序
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data

###############################################################################
def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    plt.figure(figsize=(1. * n_col, 1.26 * n_row))
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())

    #对数值归一化并以灰度图形式显示
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest', vmin=-vmax, vmax=vmax)
        plt.xticks(())  #去除子图的坐标轴标签
        plt.yticks(())
    #调整子图位置及间隔
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)


plot_gallery("First centered Olivetti faces", faces[:n_components])
###############################################################################

estimators = [
    ('Eigenfaces - PCA using randomized SVD',
         decomposition.PCA(n_components=6,whiten=True)),

    ('Non-negative components - NMF',
         decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]

###############################################################################

for name, estimator in estimators:
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    estimator.fit(faces)
    components_ = estimator.components_
    plot_gallery(name, components_[:n_components])

plt.show()

# Extracting the top 6 Eigenfaces - PCA using randomized SVD...
# (400, 4096)
# Extracting the top 6 Non-negative components - NMF...
# (400, 4096)