<h1>concurrent.futures</h1>

`concurrent.futures` 是 `3.2` 中引入的新模块，它为异步执行可调用对象提供了高层接口。
可以使用 `ThreadPoolExecutor` 来进行多线程编程，`ProcessPoolExecutor` 进行多进程编程，两者实现了同样的接口，这些接口由抽象类 `Executor` 定义。
这个模块提供了两大类型，一个是执行器类 `Executor`，另一个是 `Future` 类。
执行器用来管理工作池，`future` 用来管理工作计算出来的结果，通常不用直接操作 `future` 对象，因为有丰富的 `API`。

https://blog.csdn.net/jpch89/article/details/87643972

https://mp.weixin.qq.com/s/iERcFvg_yDQpZpAF-TFKGw