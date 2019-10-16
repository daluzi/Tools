# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/16 19:38
# @File     : python_profiler.py
# @Software : PyCharm



from cProfile import Profile
import math
def foo():
    return foo1()

def foo1():
    return foo2()

def foo2():
    return foo3()

def foo3():
    return foo4()

def foo4():
    return "this call tree seems ugly, but it always happen"

def bar():
    ret = 0
    for i in range(10000):
        ret += i * i + math.sqrt(i)
    return ret

def main():
    for i in range(100000):
        if i % 10000 == 0:
            bar()
        else:
            foo()

if __name__ == '__main__':
    prof = Profile()
    prof.runcall(main)
    prof.print_stats()
    #prof.dump_stats('test.prof') # dump profile result to test.prof

    '''
       Ordered by: standard name
    
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    99990    0.015    0.000    0.062    0.000 python_profiler.py:11(foo)
    99990    0.014    0.000    0.048    0.000 python_profiler.py:14(foo1)
    99990    0.014    0.000    0.034    0.000 python_profiler.py:17(foo2)
    99990    0.014    0.000    0.020    0.000 python_profiler.py:20(foo3)
    99990    0.006    0.000    0.006    0.000 python_profiler.py:23(foo4)
       10    0.019    0.002    0.027    0.003 python_profiler.py:26(bar)
        1    0.017    0.017    0.107    0.107 python_profiler.py:32(main)
    100000    0.009    0.000    0.009    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
    ncalls 函数总的调用次数
    tottime 函数内部（不包括子函数）的占用时间
    percall（第一个） tottime/ncalls
    cumtime 函数包括子函数所占用的时间
    percall（第二个）cumtime/ncalls
    filename:lineno(function)  文件：行号（函数）
    '''