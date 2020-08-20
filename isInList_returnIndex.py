# -*- coding: utf-8 -*-
'''
@Time    : 2020/8/20 19:29
@Author  : daluzi
@File    : isInList_returnIndex.py
'''


def find_all_index(arr, item):
    '''

    :param arr: 输入的列表
    :param item: 需要查询的元素
    :return: 返回列表中所有的待查询元素的下标
    '''
    return [i for i, a in enumerate(arr) if a == item]