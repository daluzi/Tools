<h1>pyspark</h1>



>```text
>1.hadoop的出现：
>（1）问题：1990年，电商爆发以及机器产生了大量数据，单一的系统无法承担
>（2）办法：为了解决（1）的问题许多公司，尤其是大公司领导了普通硬件集群的水平扩展
>（3）执行：hadoop应运而生
>
>2.spark的出现：
>（1）hadoop面临问题：
>     - 硬件瓶颈：多年来，内存技术突飞猛进，而硬盘技术没有太大的变化。hadoop主要
>运用的是硬盘，没有利用好内存技术。
>     - 编程困难，hadoop的MapReduce编程不太容易，后续才出现了Pig、Hive
>     - 场景不适,批处理要根据不同场景进行开发
>（2）spark应运而生
>
>3.集群的强大之处：
>（1）存储：切割   HDFS的Block
>（2）计算：切割  【分布式并行计算】 MapReduce/Spark
>（3）存储 + 计算：  HDFS/S3 + MapReduce/Spark
>```

<b>简介：</b>

```text
(1)目标：企业数据处理的统一引擎

(2)特点：
      - 广支持：一套系统解决多种环境
      - 高速度：内存上运行Hadoop快100倍，硬盘上运行比Hadoop快10倍
      - 多接口：如：Python、Java、R...
      - 多应用：sparkSQL、sparkStreaming、MLlib、GraphX

(3)为啥spark解决了hadoop慢的问题呢？
      - 减少网络使用：Spark设计思想是减少节点间的数据交互
      - 运用内存技术：Spark是和内存进行交互，Hadoop是磁盘进行交互

(4)大数据处理的三种情况：
      - 复杂的批量处理：时间长，跨度为10min~N hr
      - 历史数据为基础的交互式查询：时间通常为10sec~N min
      - 实时数据为基础的流式数据：时间通常为N ms~N sec
                   
(5)Spark的对应方案：
      - Spark Core：以RDD为基础提供了丰富的基础操作接口，
                    使得Spark可以灵活处理类似MR的批处理作业
      - Spark SQL：兼容HIVE数据，提供比Hive更快的查询速度
                   （10~100x）的分布式SQL引擎
      - Spark Streaming：将流式计算分解成一系列小的批处理作业
                         利用spark轻量级低时延的框架来支持流数
                         据处理，目前已经支持Kafka，Flume等
      - GraphX：提供图形计算框架，与Pregel/GraphLab兼容
      - MLlib：提供基于Spark的机器学习算法库
```

<b>RDD:</b>

```text
（1）RDD是什么：
    ①RDD是一个抽象类
    ②RDD支持多种类型，即泛形
    ③RDD:弹性分布式数据集
         弹性     【容错，自动进行数据的修复】
         分布式   【不同节点运行】
         数据集
                  - 不可变 （1,2,3,4,5,6）
                  - 可分区 （1,2,3)（4,5,6）
（2）RDD的特性：
    ①一个RDD由多个分区/分片组成
    ②对RDD进行一个函数操作，会对RDD的所有分区都执行相同函数操作
    ③一个RDD依赖于其他RDD，RDD1->RDD2->RDD3->RDD4->RDD5，若RDD1中某节点数据丢失，
     后面的RDD会根据前面的信息进行重新计算
    ④对于Key-Value的RDD可以制定一个partitioner，告诉他如何分片。常用hash/range
    ⑤移动数据不如移动计算，注：移动数据，不如移动计算。考虑磁盘IO和网络资源传输等
(3)图解RDD:
```

![RDD](https://pic3.zhimg.com/v2-76a15063e4d60fa98ccd6090ebd6027c_r.jpg)

```text
(4)SparkContext&SparkConf
     SparkContext意义：主入口点
     SparkContext作用：连接Spark集群
     SparkConf作用：创建SparkContext前得使用SparkConf进行配置，以键值对形式进行
     ①创建SparkContext
        - 连接到Spark“集群”：local、standalone、yarn、mesos
        - 通过SparkContext来创建RDD、广播变量到集群
     ②创建SparkContext前还需要创建SparkConf对象
     ③SparkConf().setAppName(appname).setMaster('local')这个设置高于系统设置
     ④pyspark.SparkContext连接到Spark‘集群’即master(local[单机]、Standalone[标准]
       、yarn(hadoop上)、mesos)，创建RDD，广播变量到集群
     ⑤代码：
     conf = SparkConf().setAppName(appname).setMaster('local')
     sc   = SparkContext(Conf=Conf)

(5)pyspark的使用：
    ①默认：pySpark在启动时就会创建一个SparkContext，别名为sc
           <SparkContext master = local[*] appName = PySparkShell>
    ②参数的使用：
          ./bin/pyspark --master local[4]
          ./bin/pyspark  --master[4]  --py-files code.py
  
(6)RDD的创建：
①集合转RDD
   data = [1,2,3]
   distData = sc.parallelize(data,3) #这行代码可以将列表转为RDD数据集
   distData.collect() #这行代码可以打印输出RDD数据集#【触发一个job】
   distData.reduce(lambda a,b :a+b) #【触发一个job】

   注意：一个CPU可以设置2~4个partition

②外部数据集转RDD
   distFile = sc.textFile("hello.txt") #将外部数据转换为RDD对象
   distFile.collect()

(7)提交pyspark作业到服务器上运行
   ./spark-submit --master local[2] --name spark0301 /home/hadoop/scrip
   t/spark0301.py

(8)PySpark实战之Spark Core核心RDD常用算子:
  【两个算子】
   ①transfermation： map、filter【过滤】、group by、distinct
          map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次
   ②action: count, reduce, collect
   注意：（1）
          1）All transformations in Spark are lazy，in that they do not
            compute their results right away.
            -- Spark的transformations很懒，因为他们没有马上计算出结果
          2）Instead they just remember the transformations applied to some 
            base dataset
            -- 相反，他们只记得应用于基本数据集
        （2）
          1）action triggers the computation
            -- 动作触发计算
          2） action returns values to driver or writes data to external storage
            --  action将返回值数据写入外部存储
  【单词记忆】
           applied to：施加到
           Instead：相反
           in that：因为
           external storage：外部存储


map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次
```

![map\filter](https://pic1.zhimg.com/80/v2-288572c632eefd64b4792348f4a71ec1_720w.jpg)

```text
(1)map
  map(func) 
  #将func函数作用到数据集每一个元素上，生成一个新的分布式【数据集】返回
(2)filter
  filter(func)
  返回所有func返回值为true的元素，生成一个新的分布式【数据集】返回
(3)flatMap  #flat压扁以后做map
  flatMap(func)
  输入的item能够被map或0或多个items输出，返回值是一个【Sequence】
(4)groupByKey：把相同的key的数据分发到一起
  ['hello', 'spark', 'hello', 'world', 'hello', 'world']
  ('hello',1) ('spark',1)........
(5)reduceByKey: 把相同的key的数据分发到一起并进行相应的计算
  mapRdd.reduceByKey(lambda a,b:a+b)
  [1,1]  1+1
  [1,1,1]  1+1=2+1=3
  [1]    1
(6)左连接：以左表为基准
   右连接：以右表为基准
   全连接：以左右都为基准
```