# -*- encoding: utf-8 -*-
'''
@File : 07_gradejudge.py
@Time : 2020/03/13 23:30:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#     A---成绩>=90;  
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70

import random

def gradejudge(d):
    for k, v in d.items():
        if v >= 90:
            d[k] = 'A'
        elif v >= 80 and v < 90:
            d[k] = 'B'
        elif v >= 70 and v < 80:
            d[k] = 'C'
        else:
            d[k] = 'D'

gradedict = {i : random.randint(1,100) for i in range(20)}
print("原成绩为：", end = " ")
for k, v in gradedict.items():
    print(f"{k} : {v}")

gradejudge(gradedict)
print(f"赋等级后为：", end = " ")
for k, v in gradedict.items():
    print(f"{k} : {v}")
