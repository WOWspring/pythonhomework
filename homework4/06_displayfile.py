# -*- encoding: utf-8 -*-
'''
@File : 06_displayfile.py
@Time : 2020/03/27 17:03:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小

import os

try:
    os.chdir("homework4")
except FileNotFoundError as fnf_error:
    print(fnf_error)

filelist = os.listdir()

print("名称\t日期\t类型\t大小")
for file in filelist:
    name = file
    date = os.path.getmtime(file)               #注意括号里要放上文件路径
    sort = ''
    if os.path.isdir(file):
        sort = '文件夹'
    else:
        sort = '文件'
    size = os.path.getsize(file)
    print(f'{name}\t{date}\t{sort}\t{size}')