# -*- encoding: utf-8 -*-
'''
@File : 07_countfilesize.py
@Time : 2020/03/27 17:49:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 使用python代码统计一个文件夹中所有文件的总大小

import os

try:
    os.chdir(r'pythonhomework\homework4')
except FileNotFoundError as fnf_error:
    print(fnf_error)

filelist = os.listdir()

totalsize = 0
for f in filelist:
    totalsize = totalsize + os.path.getsize(f)
print('文件总大小为%dB' %totalsize)