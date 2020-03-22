# -*- encoding: utf-8 -*-
'''
@File : open_in_sub.py
@Time : 2020/03/22 10:42:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习2 练习打开上一级目录其他子目录中的文件
import os

# 首先将工作路径设置为当前文件夹，之后再通过当前文件夹去访问其他文件夹
os.chdir('Exercise/0318/test2')
with open('../test1/test.txt', encoding = 'utf-8') as f:  #with可自动执行_end_文件的关闭
    print(f.read())
