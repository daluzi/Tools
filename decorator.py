# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/31 21:06
@Author  : daluzi
@File    : decorator.py
'''

# 定义装饰器
def decorator(func):
    def wrapper(*args, **kargs):
        # 可以自定义传入的参数
       print(func.__name__)
        # 返回传入的方法名参数的调用
       return func(*args, **kargs)

    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(1, 2))