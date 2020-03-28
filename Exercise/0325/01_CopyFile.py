# -*- encoding: utf-8 -*-
'''
@File : 01_CopyFile.py
@Time : 2020/03/25 08:42:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
#待完成
#写一个copy函数，用于复制文件

import os

os.chdir(r"Exercise\0325\targetfile1")
#

def copy(x, tf2):
    content = []
    # print(x)
    # if os.path.isdir(tf2):
    #     print("1")
    # else :
    #     print("22")
    with open(x, 'r', encoding = 'utf-8') as f:
        content = f.readlines()
    newfn = os.path.join(tf2,x)
    #print(newfn)
    with open(newfn, 'w', encoding = 'utf-8') as f:
        f.writelines(content)
    #会报错，显示没有这个路径
    # with open(os.path.join(tf2,x), 'w', encoding = 'utf-8') as f:
    #     f.writelines(newfn)

tf2 = r"..\targetfile2"     #解决问题，os的chdir使用的是相对路径，如果tf2也要使用相对路径的话，应该以cwd为基础，通过..去访问父目录
flist = os.listdir()
#print(flist)

for x in flist:
    if os.path.isdir(x):
        pass
    else:
        copy(x, tf2)