# -*- encoding: utf-8 -*-
'''
@File : 02_readinput.py
@Time : 2020/03/23 16:39:29
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
# #第一行： xxxx
# #第二行： xxxx
import os

try:
    os.chdir("homework3")
except FileNotFoundError as fnf_error:
    print(fnf_error)

try:
    with open("input.txt", 'r', encoding = 'utf-8') as f:
        temp = f.readline()
        count = 1
        while len(temp) > 0:
            print(f"#第{count}行： {temp}")
            count = count + 1
            temp = f.readline()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')