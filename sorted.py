# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/9/26 22:16
# @File     : sorted.py
# @Software : PyCharm

'''
	sorted(L)返回一个排序后的L，不改变原始的L；
	L.sort()是对原始的L进行操作，调用后原始的L会改变，没有返回值。【所以a = a.sort()是错的啦！a = sorted(a)才对！
	sorted()适用于任何可迭代容器，list.sort()仅支持list（本身就是list的一个方法）
'''



## 1、最简单的排序
l = [5,2,3,1,4 ]
l .sort()
print(l)   ##输出：[1, 2, 3, 4, 5]

l.sort(reverse=True)#反序
print(l)    ##输出：[5, 4, 3, 2, 1]

##2、字符串排序
StrList = ['Fast', 'Smooth', 'fast', 'is', 'is', 'smooth']
# 2.1 一般字典序排列，但是大写在前，小写在后！！
StrList.sort()
print(StrList) ##字符串列表是按照第一个字符的大小排序的
##输出：['Fast', 'Smooth', 'fast', 'is', 'is', 'smooth']

# 2.2忽略大小写，按abcd顺序
StrList.sort(key=str.lower)
print(StrList) ##输出：['Fast', 'fast', 'is', 'is', 'Smooth', 'smooth']

# 2.3按照字符串长度排序
StrList.sort(key=len)
print(StrList)##输出：['is', 'is', 'fast', 'Fast', 'Smooth', 'smooth']

StrList.sort(key=len, reverse=True)#反序
print(StrList) ##输出：['Smooth', 'smooth', 'fast', 'Fast', 'is', 'is']


#sort配合lambda()
l = [[2, 2, 3], [1, 4, 5], [5, 4, 9]]
l.sort(key=lambda x: x[0])  ##按照第一个元素进行排序
print(l)  ##输出：[[1, 4, 5], [2, 2, 3], [5, 4, 9]]
'''
    匿名函数的x，表示的是l列表中的每一个成员元素

    x[0] :表示列表里面列表的第一个成员元素
'''



class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
ss = sorted(student_objects, key=lambda student: student.age)   # sort by age
print(ss)#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

#如果第一个排序条件相同，则按照第二个条件排序
a = [[2,3],[4,1],(2,8),(2,1),(3,4)]
b = sorted(a,key=lambda x: (x[0], x[1]))
print(b)#[(2, 1), [2, 3], (2, 8), (3, 4), [4, 1]]

## 面试很可能会遇到
dic = {'a': 2, 'b': 1}

# 1、按照key排序
d = sorted(dic.keys() , key = lambda k: k[0])
print(d)
# 2、按照values排序
e = sorted(dic.items() , key = lambda k: k[1])
print(e)
#key和values互换
print({values:key for key,values in dic.items()})

#方法二
import operator

# 初始化字典

dict_data = {6: 9, 10: 5, 3: 11, 8: 2, 7: 6}

# 按键（key）进行排序
test_data_4 = sorted(dict_data.items(), key=operator.itemgetter(0))
test_data_5 = sorted(dict_data.items(), key=operator.itemgetter(0), reverse=True)

print(test_data_4)  # [(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]
print(test_data_5)  # [(10, 5), (8, 2), (7, 6), (6, 9), (3, 11)]

# 按值（value）进行排序

test_data_6 = sorted(dict_data.items(), key=operator.itemgetter(1))

test_data_7 = sorted(dict_data.items(), key=operator.itemgetter(1), reverse=True)

print(test_data_6)  # [(8, 2), (10, 5), (7, 6), (6, 9), (3, 11)]

print(test_data_7)  # [(3, 11), (6, 9), (7, 6), (10, 5), (8, 2)]