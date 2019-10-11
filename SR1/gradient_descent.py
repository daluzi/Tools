# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/11 19:00
# @File     : gradient_descent.py
# @Software : PyCharm

# import numpy as np
# import matplotlib.pyplot as plt
# #y=2 * (x1) + (x2) + 3
# rate = 0.001
# x_train = np.array([    [1, 2],    [2, 1],    [2, 3],    [3, 5],    [1, 3],    [4, 2],    [7, 3],    [4, 5],    [11, 3],    [8, 7]    ])
# y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
# x_test  = np.array([    [1, 4],    [2, 2],    [2, 5],    [5, 3],    [1, 5],    [4, 1]    ])
#
# a = np.random.normal()
# b = np.random.normal()
# c = np.random.normal()
#
# def h(x):
#     return a*x[0]+b*x[1]+c
#
# for i in range(10000):
#     sum_a=0
#     sum_b=0
#     sum_c=0
#     for x, y in zip(x_train, y_train):
#         sum_a = sum_a + rate*(y-h(x))*x[0]
#         sum_b = sum_b + rate*(y-h(x))*x[1]
#         sum_c = sum_c + rate*(y-h(x))
#     a = a + sum_a
#     b = b + sum_b
#     c = c + sum_c
#     plt.plot([h(xi) for xi in x_test])
#
# print(a)
# print(b)
# print(c)
#
# result=[h(xi) for xi in x_train]
# print(result)
#
# result=[h(xi) for xi in x_test]
# print(result)
#
# plt.show()


'''
梯度下降算法
Batch Gradient Descent
Stochastic Gradient Descent SGD
'''
__author__ = 'epleone'
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

# 使用随机数种子， 让每次的随机数生成相同，方便调试
# np.random.seed(111111111)


class GradientDescent(object):
    eps = 1.0e-8
    max_iter = 1000000  # 暂时不需要
    dim = 1
    func_args = [2.1, 2.7]  # [w_0, .., w_dim, b]

    def __init__(self, func_arg=None, N=1000):
        self.data_num = N
        if func_arg is not None:
            self.FuncArgs = func_arg
        self._getData()

    def _getData(self):
        x = 20 * (np.random.rand(self.data_num, self.dim) - 0.5)
        b_1 = np.ones((self.data_num, 1), dtype=np.float)
        # x = np.concatenate((x, b_1), axis=1)
        self.x = np.concatenate((x, b_1), axis=1)

    def func(self, x):
        # noise太大的话， 梯度下降法失去作用
        noise = 0.01 * np.random.randn(self.data_num) + 0
        w = np.array(self.func_args)
        # y1 = w * self.x[0, ]    # 直接相乘
        y = np.dot(self.x, w)  # 矩阵乘法
        y += noise
        return y

    @property
    def FuncArgs(self):
        return self.func_args

    @FuncArgs.setter
    def FuncArgs(self, args):
        if not isinstance(args, list):
            raise Exception(
                'args is not list, it should be like [w_0, ..., w_dim, b]')
        if len(args) == 0:
            raise Exception('args is empty list!!')
        if len(args) == 1:
            args.append(0.0)
        self.func_args = args
        self.dim = len(args) - 1
        self._getData()

    @property
    def EPS(self):
        return self.eps

    @EPS.setter
    def EPS(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise Exception("The type of eps should be an float number")
        self.eps = value

    def plotFunc(self):
        # 一维画图
        if self.dim == 1:
            # x = np.sort(self.x, axis=0)
            x = self.x
            y = self.func(x)
            fig, ax = plt.subplots()
            ax.plot(x, y, 'o')
            ax.set(xlabel='x ', ylabel='y', title='Loss Curve')
            ax.grid()
            plt.show()
        # 二维画图
        if self.dim == 2:
            # x = np.sort(self.x, axis=0)
            x = self.x
            y = self.func(x)
            xs = x[:, 0]
            ys = x[:, 1]
            zs = y
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(xs, ys, zs, c='r', marker='o')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
            plt.show()
        else:
            # plt.axis('off')
            plt.text(
                0.5,
                0.5,
                "The dimension(x.dim > 2) \n is too high to draw",
                size=17,
                rotation=0.,
                ha="center",
                va="center",
                bbox=dict(
                    boxstyle="round",
                    ec=(1., 0.5, 0.5),
                    fc=(1., 0.8, 0.8), ))
            plt.draw()
            plt.show()
            # print('The dimension(x.dim > 2) is too high to draw')

    # 梯度下降法只能求解凸函数
    def _gradient_descent(self, bs, lr, epoch):
        x = self.x
        # shuffle数据集没有必要
        # np.random.shuffle(x)
        y = self.func(x)
        w = np.ones((self.dim + 1, 1), dtype=float)
        for e in range(epoch):
            print('epoch:' + str(e), end=',')
            # 批量梯度下降，bs为1时 等价单样本梯度下降
            for i in range(0, self.data_num, bs):
                y_ = np.dot(x[i:i + bs], w)
                loss = y_ - y[i:i + bs].reshape(-1, 1)
                d = loss * x[i:i + bs]
                d = d.sum(axis=0) / bs
                d = lr * d
                d.shape = (-1, 1)
                w = w - d

            y_ = np.dot(self.x, w)
            loss_ = abs((y_ - y).sum())
            print('\tLoss = ' + str(loss_))
            print('拟合的结果为:', end=',')
            print(sum(w.tolist(), []))
            print()
            if loss_ < self.eps:
                print('The Gradient Descent algorithm has converged!!\n')
                break
        pass

    def __call__(self, bs=1, lr=0.1, epoch=10):
        if sys.version_info < (3, 4):
            raise RuntimeError('At least Python 3.4 is required')
        if not isinstance(bs, int) or not isinstance(epoch, int):
            raise Exception(
                "The type of BatchSize/Epoch should be an integer number")
        self._gradient_descent(bs, lr, epoch)
        pass

    pass


if __name__ == "__main__":
    if sys.version_info < (3, 4):
        raise RuntimeError('At least Python 3.4 is required')

    gd = GradientDescent([1.2, 1.4, 2.1, 4.5, 2.1])
    # gd = GradientDescent([1.2, 1.4, 2.1])
    print("要拟合的参数结果是: ")
    print(gd.FuncArgs)
    print("===================\n\n")
    # gd.EPS = 0.0
    gd.plotFunc()
    gd(10, 0.01)
    print("Finished!")
