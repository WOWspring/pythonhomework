# -*- encoding: utf-8 -*-
'''
@File : read_test.py
@Time : 2020/03/22 11:01:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习3 读取score.txt文件中内容
from os import chdir

# vscode默认的工作路径为项目的根路径
# 将工作路径切换到本文件所在目录
chdir('Exercise/0318')
with open('stuinfo.txt', 'r', encoding='utf-8') as file:
    res = file.readline()
    while len(res) > 0:
        print(res, end='')
        res = file.readline()
