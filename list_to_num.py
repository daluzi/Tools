# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/12/2 22:54
# @File     : list_to_num.py
# @Software : PyCharm

numbers = ['1', '5', '10', '8'] ## 	numbers = [1, 5, 10, 8]

new_numbers = []
for n in numbers:
	new_numbers.append(int(n))
numbers = new_numbers

numbers = [int(x) for x in numbers]

numbers = list(map(int, numbers))