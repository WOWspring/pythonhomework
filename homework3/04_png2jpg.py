# -*- encoding: utf-8 -*-
'''
@File : 04_png2jpg.py
@Time : 2020/03/23 20:12:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.

#利用网上看到的os模块相应知识进行操作

import os

try:
    os.chdir("homework3\img")
except FileNotFoundError as fnf_error:
    print(fnf_error)

filelist = os.listdir()
print(filelist)         #test
for f in filelist:
    newlastn = ''
    port = os.path.splitext(f)
    try:
        if port[1] == '.png':
            newlastn = port[0] + '.jpg'
            os.rename(f,newlastn)           #错误WinError3，系统找不到指定的路径。: '15we.word' -> '
    except FileNotFoundError as fnf_error:
        print(fnf_error)

