# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/16 21:08
# @File     : practical_pythonic.py
# @Software : PyCharm

# 生成器可以简单理解成一个函数，每次执行到 yield 语句就返回一个值，通过不停地调用这个函数，就能获取到所有的值，这些值就能构成了一个等效的列表，但是与列表不同的是，这些值是不断计算得出，而列表是在一开始就计算好了，这就是 lazy evaluation 的思想。
def fibonacci():
    num0 = 0
    num1 = 1
    for i in range(10):
        num2 = num0 + num1
        yield num2
        num0 = num1
        num1 = num2

for i in fibonacci():
    print(i)
print(list(fibonacci()))


# pythonic 写法
#在 python 里面，else 还可以用在循环和异常里面。else 放在循环里面的含义是，如果循环全部遍历完成，没有执行 break，则执行 else 子句
for cc in ['UK', 'ID', 'JP', 'US']:
    if cc == 'CN':
        break
else:
    print('no CN')

# 一般写法
no_cn = True
for cc in ['UK', 'ID', 'JP', 'US']:
    if cc == 'CN':
        no_cn = False
        break
if no_cn:
    print('no CN')

# # pythonic 写法
# try:
#     db.execute('UPDATE table SET xx=xx WHERE yy=yy')
# except DBError:
#     db.rollback()
# else:
#     db.commit()
#
# # 一般写法
# has_error = False
# try:
#     db.execute('UPDATE table SET xx=xx WHERE yy=yy')
# except DBError:
#     db.rollback()
#     has_error = True
# if not has_error:
#     db.commit()

'''
使用 with as 语句后，无需手动调用 fp.close(), 在作用域结束后，文件会被自动 close 掉，完整的执行过如下:

1.调用 open('pythonic.py')，返回的一个对象 obj,
2.调用 obj.__enter__() 方法，返回的值赋给 fp
3.执行 with 中的代码块
4.执行 obj.__exit__()
5.如果这个过程发生异常，将异常传给 obj.__exit__()，如果 obj.__exit__() 返回 False, 异常将被继续抛出，如果返回 True，异常被挂起，程序继续运行
'''
# # pythonic 写法
# with open('pythonic.py') as fp:
#     for line in fp:
#         print(line[:-1])
#
# # 一般写法
# fp = open('pythonic.py')
# for line in fp:
#     print(line[:-1])
# fp.close()

# 列表推导与生成器表达式
# pythonic 写法
squares = [x * x for x in range(10)]

# 一般写法
squares1 = []
for x in range(10):
    squares1.append(x * x)


# python 里面 map 的遍历有很多种方式，在需要同事使用 key 和 value 的场合，建议使用 items() 函数
m = {'one': 1, 'two': 2, 'three': 3}
for k, v in m.items():
    print(k, v)

for k, v in sorted(m.items()):
    print(k, v)

