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
