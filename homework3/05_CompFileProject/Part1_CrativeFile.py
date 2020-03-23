# -*- encoding: utf-8 -*-
'''
@File : Part1_crtfile.py
@Time : 2020/03/23 20:39:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 创建一个文件综合变成迷你项目
# 1、创建一个文件Blowing in the wind.txt ，且输入歌词
# 2、在文件头部插入歌名"Blowin' in the wind"
# 3、在歌名后插入歌手名"Bob Dylan"
# 4、在文件末尾加上字符串“1962 by Warner Bros.Inc.”
# 5、在屏幕上打印文件内容

#该程序完成第一部分

import os
txt = """How many roads must a man walk down
Before they call him a man 
How many seas must a white dove sail 
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer, my friend, is blowing in the wind
The answer is blowing in the wind
"""
txtlist = txt.split('\n')
#print(txtlist)
try:
    os.chdir(r"homework3\05_CompFileProject")
except FileNotFoundError as fnf_error:
    print(fnf_error)

try:
    with open("Blowing in the wind.txt", 'w', encoding = 'utf-8') as f:
        #pass
        for temp in txtlist:
            f.write(temp + '\n')
except FileNotFoundError as fnf_error:
    print(fnf_error)