# -*- encoding: utf-8 -*-
'''
@File : Part3_InsertSinger.py
@Time : 2020/03/23 22:47:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# here put the import lib
# here put the import lib
# 创建一个文件综合变成迷你项目
# 1、创建一个文件Blowing in the wind.txt ，且输入歌词
# 2、在文件头部插入歌名"Blowin' in the wind"
# 3、在歌名后插入歌手名"Bob Dylan"
# 4、在文件末尾加上字符串“1962 by Warner Bros.Inc.”
# 5、在屏幕上打印文件内容

#该程序完成第三部分

import os

try:
    os.chdir(r"homework3\05_CompFileProject")
except FileNotFoundError as fnf_error:
    print(fnf_error)

try:
    with open("Blowing in the wind.txt", 'r+', encoding = 'utf-8') as f:
        Song = f.readline()
        oldtxt = f.read()
        f.seek(0)
        f.write(Song.strip('\n') + "\t\t\tBob Dylan\n")
        f.write(oldtxt)
except FileNotFoundError as fnf_error:
    print(fnf_error)