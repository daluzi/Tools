import random_test
import tkinter
import numpy
from click import command
from numpy import mat
from numpy import zeros

root = tkinter.Tk()

# 框架定义：master为root且长40 宽30
frm1 = tkinter.LabelFrame(root, text="计算模糊规则（从A到B）", padx=40, pady=30)
frm2 = tkinter.LabelFrame(root, text="输入事实并得到结论", padx=40, pady=30)
frm1.pack()
frm2.pack()
root.title("模糊管理")
v1 = tkinter.StringVar()
v2 = tkinter.StringVar()
v3 = tkinter.StringVar()
v4 = tkinter.StringVar()
# 在frm1框架中定义两个标签
tkinter.Label(frm1, text="输入A：").grid(row=0, column=0)
tkinter.Label(frm1, text="输入B：").grid(row=1, column=0)
# 在frm2中定义标签
tkinter.Label(frm2, text="输入A'：").grid(row=3, column=0)
e1 = tkinter.Entry(frm1, textvariable=v1).grid(row=0, column=1, padx=10, pady=10)
e2 = tkinter.Entry(frm1, textvariable=v2).grid(row=1, column=1, padx=10, pady=10)
e3 = tkinter.Entry(frm2, textvariable=v3).grid(row=3, column=1, padx=10, pady=10)
e4 = tkinter.Entry(frm2, textvariable=v4).grid(row=4, column=1, padx=10, pady=10)
ll = tkinter.Label(frm1).grid(row=4, column=1, padx=10, pady=10)



def CFRM():
    # 以，作为分隔符，将v1存入LSD1
    LSD1 = v1.get().split(',')
    LSD2 = v2.get().split(',')
    i = -1
    j = -1
    # 将LSD中的数据转换为float类型
    for x in LSD1:
        i = i+1
        LSD1[i] = float(LSD1[i])
    for y in LSD2:
        j = j+1
        LSD2[j] = float(LSD2[j])
    global FRM
    # FRM定义为一个矩阵，初始化为0，len（LSD1）*len（LSD2）
    FRM = mat(numpy.zeros((len(LSD1), len(LSD1))))
    i = 0
    while i < len(LSD1):
        j = 0
        while j < len(LSD1):
            FRM[i, j] = max([min([LSD1[i], LSD2[j]]), 1-LSD1[i]])
            j = j+1
        i = i+1
    print(FRM)
    t = tkinter.Text(frm1, width=30, height=5)
    t.grid(row=2, column=1)
    t.insert(tkinter.END, FRM)


bot = tkinter.Button(frm1, text="计算模糊关系矩阵：", command=CFRM).grid(row=2, column=0)
bot1 = tkinter.Button(frm2, text="计算B':").grid(row=4, column=0)
root.mainloop()
