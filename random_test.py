# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/17 12:55
# @File     : random_test.py
# @Software : PyCharm

import random
lie = 10
randomResult = random.sample(range(1, lie), int(0.2 * lie))
print(randomResult)