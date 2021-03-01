<h1>PyTorch</h1>

> * 上手快，掌握 Numpy 和基本深度学习概念即可上手。
> * 代码简洁灵活，使用 nn.Module 封装使得网络搭建更加方便 。基于动态图机制，更加灵活。
> * 资源多，arXiv 中新论文的算法大多有 PyTorch 实现。
> * 开发者多，Github 上贡献者(Contributors)已经超过 1100+

五大要素：

1. 数据：包括数据读取，数据清洗，进行数据划分和数据预处理，比如读取图片如何预处理及数据增强。
2. 模型：包括构建模型模块，组织复杂网络，初始化网络参数，定义网络层。
3. 损失函数：包括创建损失函数，设置损失函数超参数，根据不同任务选择合适的损失函数。
4. 优化器：包括根据梯度使用某种优化器更新参数，管理模型参数，管理多个参数组实现不同学习率，调整学习率。
5. 迭代训练：组织上面 4 个模块进行反复训练。包括观察训练效果，绘制 Loss/ Accuracy 曲线，用 TensorBoard 进行可视化分析。

> 可以使用此命令查看是否有GPU，我木有。。
>
> ![image-20210301142215475](C:\Users\daluzi\AppData\Roaming\Typora\typora-user-images\image-20210301142215475.png)

---



<b>Tensor:</b>

Tensor 中文为张量。张量的意思是一个多维数组，它是标量、向量、矩阵的高维扩展。

标量可以称为 0 维张量，向量可以称为 1 维张量，矩阵可以称为 2 维张量，RGB 图像可以表示 3 维张量。你可以把张量看作多维数组。

![img](https://image.zhangxiann.com/20200515144610.png)



将0.4.0以前的版本做了修改之后，目前的Tensor具有8个属性：

<img src="https://image.zhangxiann.com/20200515145801.png" alt="img" style="zoom:50%;" />

* data: 被包装的 Tensor。
* grad: data 的梯度。
* grad_fn: 创建 Tensor 所使用的 Function，是自动求导的关键，因为根据所记录的函数才能计算出导数。
* requires_grad: 指示是否需要梯度，并不是所有的张量都需要计算梯度。
* is_leaf: 指示是否叶子节点(张量)，叶子节点的概念在计算图中会用到，后面详细介绍。
* dtype: 张量的数据类型，如 torch.FloatTensor，torch.cuda.FloatTensor。
* shape: 张量的形状。如 (64, 3, 224, 224)
* device: 张量所在设备 (CPU/GPU)，GPU 是加速计算的关键

> 关于 dtype，PyTorch 提供了 9 种数据类型，共分为 3 大类：float (16-bit, 32-bit, 64-bit)、integer (unsigned-8-bit ,8-bit, 16-bit, 32-bit, 64-bit)、Boolean。模型参数和数据用的最多的类型是 float-32-bit。label 常用的类型是 integer-64-bit。



<b>Tensor的创建方式：</b>

1. 直接创建Tensor：[torch.tensor()](#torch.tensor); [torch.from_numpy(ndarray)](#torch.from_numpy(ndarray));
2. 根据数值创建Tensor：[torch.zeros()](#torch.zeros()); [torch.zeros_like](#torch.zeros_like); [torch.full()](#torch.full()); [torch.full_like()](#torch.full_like()); [torch.arange()](#torch.arange()); [torch.linspace()](#torch.linspace()); [torch.logspace()](#torch.logspace()); [torch.eye()](#torch.eye());
3. 根据概率创建Tensor：[troch.normal()](#troch.normal()); [torch.randn()](#torch.randn()); [torch.randn_like()](#torch.randn_like()); [torch.rand()](#torch.rand()); [torch.rand_like()](#torch.rand_like()); [torch.randint()](#torch.randint()); [troch.randint_like()](#troch.randint_like()); [torch.randperm()](#torch.randperm()); [torch.bernoulli()](#torch.bernoulli());



<span id="torch.tensor">troch.tensor</span>

```python
torch.tensor(data, dtype=None, device=None, requires_grad=False, pin_memory=False)
```

> data: 数据，可以是 list，numpy
>
> dtype: 数据类型，默认与 data 的一致
>
> device: 所在设备，cuda/cpu
>
> requires_grad: 是否需要梯度
>
> pin_memory: 是否存于锁页内存

```python
import torch
import numpy as np

arr = np.ones((3, 3))
print("ndarray的数据类型：", arr.dtype)
t = torch.tensor(arr)
print(t)

//
输出为：
ndarray的数据类型： float64
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)
```



<span id="torch.from_numpy(ndarray)">troch.from_numpy(ndarray)</span>

从 numpy 创建 tensor。利用这个方法创建的 tensor 和原来的 ndarray 共享内存，当修改其中一个数据，另外一个也会被改动。

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
t = torch.from_numpy(arr)

# 修改 array，tensor 也会被修改
# print("\n修改arr")
# arr[0, 0] = 0
# print("numpy array: ", arr)
# print("tensor : ", t)

# 修改 tensor，array 也会被修改
print("\n修改tensor")
t[0, 0] = -1
print("numpy array: ", arr)
print("tensor : ", t)

//
输出为：
修改tensor
numpy array:  [[-1  2  3]
 [ 4  5  6]]
tensor :  tensor([[-1,  2,  3],
        [ 4,  5,  6]], dtype=torch.int32)
```



<span id="torch.zeros()">torch.zeros()</span>

```python
torch.zeros(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>size: 张量的形状
>
>out: 输出的张量，如果指定了 out，那么`torch.zeros()`返回的张量和 out 指向的是同一个地址
>
>layout: 内存中布局形式，有 strided，sparse_coo 等。当是稀疏矩阵时，设置为 sparse_coo 可以减少内存占用。
>
>device: 所在设备，cuda/cpu
>
>requires_grad: 是否需要梯度

```python
out_t = torch.tensor([1])
# 这里制定了 out
t = torch.zeros((3, 3), out=out_t)
print(t, '\n', out_t)
# id 是取内存地址。最终 t 和 out_t 是同一个内存地址
print(id(t), id(out_t), id(t) == id(out_t))

//
输出为：
tensor([[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]) 
 tensor([[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]])
2984903203072 2984903203072 True
```



<span id="torch.zeros_like">torch.zeros_like</span>

```python
torch.zeros_like(input, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)
```

>功能：根据 input 形状创建全 0 张量
>
>input: 创建与 input 同形状的全 0 张量
>
>dtype: 数据类型
>
>layout: 内存中布局形式，有 strided，sparse_coo 等。当是稀疏矩阵时，设置为 sparse_coo 可以减少内存占用。
>
>同理还有全 1 张量的创建方法：`torch.ones()`，`torch.ones_like()`。



<span id="torch.full()">torch.full() </span>    <span id="torch.full_like()">torch.full_like()</span>

```python
torch.full(size, fill_value, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：创建自定义数值的张量 
>
>size: 张量的形状，如 (3,3)
>
>fill_value: 张量中每一个元素的值

```python
t = torch.full((3, 3), 1)
print(t)

//输出为：
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
```



<span id="torch.arange()">torch.arange()</span>

```python
torch.arange(start=0, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：创建等差的 1 维张量。注意区间为[start, end)。
>
>start: 数列起始值
>
>end: 数列结束值，开区间，取不到结束值
>
>step: 数列公差，默认为 1

```python
t = torch.arange(2, 10, 2)
print(t)

//
输出为：
tensor([2, 4, 6, 8])
```



<span id="torch.linspace()">torch.linspace()</span>

```python
torch.linspace(start, end, steps=100, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：创建均分的 1 维张量。数值区间为 [start, end]
>
>start: 数列起始值
>
>end: 数列结束值
>
>steps: 数列长度 (元素个数)

```python
t = torch.linspace(2, 10, 6)
print(t)

//
输出为：
tensor([ 2.0000,  3.6000,  5.2000,  6.8000,  8.4000, 10.0000])
```



<span id="torch.logspace()">torch.logspace()</span>

```python
torch.logspace(start, end, steps=100, base=10.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：创建对数均分的 1 维张量。数值区间为 [start, end]，底为 base。
>
>start: 数列起始值
>
>end: 数列结束值
>
>steps: 数列长度 (元素个数)
>
>base: 对数函数的底，默认为 10

```python
t = torch.linspace(2, 10, 6)
print(t)

//
输出为：
tensor([ 2.0000,  3.6000,  5.2000,  6.8000,  8.4000, 10.0000])
```



<span id="torch.eye()">torch.eye()</span>

```python
torch.eye(n, m=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：创建单位对角矩阵( 2 维张量)，默认为方阵
>
>n: 矩阵行数。通常只设置 n，为方阵。
>
>m: 矩阵列数



<span id="troch.normal()">troch.normal()</span>

```python
torch.normal(mean, std, *, generator=None, out=None)
```

>功能：生成正态分布 (高斯分布)
>
>mean: 均值
>
>std: 标准差

有 4 种模式：

1. mean 为标量，std 为标量。这时需要设置 size。

   代码示例：

   ```python
   # mean：标量 std: 标量
   # 这里需要设置 size
   t_normal = torch.normal(0., 1., size=(4,))
   print(t_normal)
   ```

   输出为：

   ```python
   tensor([0.6614, 0.2669, 0.0617, 0.6213])
   ```

2. mean 为标量，std 为张量

3. mean 为张量，std 为标量

   代码示例：

   ```python
   # mean：张量 std: 标量
   mean = torch.arange(1, 5, dtype=torch.float)
   std = 1
   t_normal = torch.normal(mean, std)
   print("mean:{}\nstd:{}".format(mean, std))
   print(t_normal)
   ```

   输出为：

   ```python
   mean:tensor([1., 2., 3., 4.])
   std:1
   tensor([1.6614, 2.2669, 3.0617, 4.6213])
   ```

   这 4 个数采样分布的均值不同，但是方差都是 1。

4. mean 为张量，std 为张量

   代码示例：

   ```python
   # mean：张量 std: 张量
   mean = torch.arange(1, 5, dtype=torch.float)
   std = torch.arange(1, 5, dtype=torch.float)
   t_normal = torch.normal(mean, std)
   print("mean:{}\nstd:{}".format(mean, std))
   print(t_normal)
   ```

   输出为：

   ```python
   mean:tensor([1., 2., 3., 4.])
   std:tensor([1., 2., 3., 4.])
   tensor([1.6614, 2.5338, 3.1850, 6.4853])
   ```

   其中 1.6614 是从正态分布 $N(1,1)$ 中采样得到的，其他数字以此类推。

   

<span id="torch.randn()">torch.randn()</span>  <span id="torch.randn_like()">torch.randn_like()</span>

```python
torch.randn(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：生成标准正态分布。
>
>size: 张量的形状



<span id="torch.rand()">torch.rand()</span>  <span id="torch.rand_like()">torch.rand_like()</span>

```python
torch.rand(*size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

> 功能：在区间 [0, 1) 上生成均匀分布。



<span id="torch.randint()">torch.randint()</span>  <span id="troch.randint_like()">troch.randint_like()</span>

```python
randint(low=0, high, size, *, generator=None, out=None,
dtype=None, layout=torch.strided, device=None, requires_grad=False)
```

>功能：在区间 [low, high) 上生成整数均匀分布。
>
>size: 张量的形状



<span id="torch.randperm()">torch.randperm()</span>

```python
torch.randperm(n, out=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False)
```

>功能：生成从 0 到 n-1 的随机排列。常用于生成索引。
>
>n: 张量的长度



<span id="torch.bernoulli()">torch.bernoulli()</span>

```python
torch.bernoulli(input, *, generator=None, out=None)
```

>功能：以 input 为概率，生成伯努利分布 (0-1 分布，两点分布)
>
>input: 概率值

---



<b>张量的操作：</b>

1. 拼接：torch.cat(); torch.stack(); 
2. 切分：torch.chunk(); torch.split(); 
3. 索引：torch.index_select(); torch.masked_select();
4. 变换：torch.reshape(); torch.transpose(); torch.t(); torch.squeeze(); torch.unsqueeze();

<b>张量的数学运算：</b>

主要分为 3 类：加减乘除，对数，指数，幂函数 和三角函数。

如：torch.add(); torch.addcdiv(); torch.addcmul(); 

