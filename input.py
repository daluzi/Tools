# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/15 16:07
@Author  : daluzi
@File    : input.py
'''


#实现回车换行，而不是结束
endstr="end"#重新定义结束符
str=""
for line in iter(input,endstr):#每行接收的东西 用了iter的哨兵模式
    str+= line+"\n"#换行
print(str)