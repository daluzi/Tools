# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/11/13 9:34
# @File     : integer_division.py
# @Software : PyCharm

n = int(input("请输入秒数："))
day = 0
hour = 0
minute = 0
if n>=3600*24:
          # day = int(n / 3600 / 24)
		  # python整数除法为//
          day = n // 3600 // 24
          n = n - day * 3600 * 24
          hour = int(n /3600)
          n = n - hour * 3600
          minute = int(n / 60)
          n = n - minute * 60
elif n<3600 * 24 and n >= 3600:
          hour = n /3600
          n = n - hour * 3600
          minute = n / 60
          n = n - minute * 60
elif n < 3600 and n>=60:
          minute = n / 60
          n = n - minute * 60
else:
          n = n
print("%d: %d: %d :%d" %(day, hour, minute, n))