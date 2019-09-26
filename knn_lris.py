# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/9/26 14:20
# @File     : knn_lris.py
# @Software : PyCharm

from sklearn import datasets
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

iris=datasets.load_iris()#加载数据集
print(iris.data,iris.target,iris.target_names)#查看数据集数据和类别

# x=iris.data[:,0]
# y=iris.data[:,1]
x=iris.data[:,2]
y=iris.data[:,3]

species=iris.target
x_min,x_max=x.min()-0.5,x.max()+0.5
y_min,y_max=y.min()-0.5,y.max()+0.5

plt.figure()
plt.title('基于iris数据集的kNN')#设置题目
plt.scatter(x,y,c=species)

plt.xlim(x_min,x_max)#设置x轴刻度的取值范围
plt.ylim(y_min,y_max)
plt.xlabel('萼片长度')#设置x轴标签
plt.ylabel('萼片宽度')
plt.xticks(())#设置x轴文本
plt.yticks(())
plt.show()


from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier#导入分类器

np.random.seed(0)
iris=datasets.load_iris()

x=iris.data
y=iris.target
i=np.random.permutation(len(iris.data))#打乱顺序

x_train=x[i[:-10]]#前140做训练集，剩余10做测试集
y_train=y[i[:-10]]
x_text=x[i[-10:]]
y_text=y[i[-10:]]

knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
print(knn.predict(x_text),y_text)


#画边界代码
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.neighbors import KNeighborsClassifier#导入分类器
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

iris=datasets.load_iris()
x=iris.data[:,:2]
y=iris.target

x_min,x_max=x[:,0].min()-0.5,x[:,0].max()+0.5
y_min,y_max=x[:,1].min()-0.5,x[:,1].max()+0.5

cmap_light=ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h=0.02
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

knn=KNeighborsClassifier()
knn.fit(x,y)
z=knn.predict(np.c_[xx.ravel(),yy.ravel()])
z=z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,z,cmap=cmap_light)

plt.title('基于Iris数据集的kNN')
plt.scatter(x[:,0],x[:,1],c=y)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.xlabel('萼片长度')
plt.ylabel('萼片宽度')
plt.show()


#画边界代码
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.neighbors import KNeighborsClassifier#导入分类器
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

iris=datasets.load_iris()
x=iris.data[:,:2]
y=iris.target

x_min,x_max=x[:,0].min()-0.5,x[:,0].max()+0.5
y_min,y_max=x[:,1].min()-0.5,x[:,1].max()+0.5

cmap_light=ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h=0.02
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

knn=KNeighborsClassifier()
knn.fit(x,y)
z=knn.predict(np.c_[xx.ravel(),yy.ravel()])
z=z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,z,cmap=cmap_light)

plt.title('基于Iris数据集的kNN')
plt.scatter(x[:,0],x[:,1],c=y)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.xlabel('萼片长度')
plt.ylabel('萼片宽度')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

y[::5] += 1 * (0.5 - np.random.rand(8))#噪音

n_neighbors = 5

for i, weights in enumerate(['uniform', 'distance']):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, c='k', label='data')
    plt.plot(T, y_, c='g', label='prediction')
    plt.axis('tight')
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,
                                                                weights))

plt.show()

