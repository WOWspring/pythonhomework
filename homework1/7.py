# -*- encoding: utf-8 -*-
'''
@File : 7.py
@Time : 2020/03/05 16:57:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question:  打印输出9*9乘法表，按照下面的格式：

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}", end = "  ")
    print("\n")

