# -*- encoding: utf-8 -*-
'''
@File : open_test.py
@Time : 2020/03/22 10:44:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习2 打开同级文件和子目录中的文件
import os

# 首先将工作路径设置为当前文件夹，之后再通过当前文件夹去访问其他文件夹
os.chdir('Exercise/0318')

# 同级文件
# open函数默认的编码形式就是encoding
# 但vscode创建的文本文件编码为UTF-8，需要设置encoding的参数
with open('os_path_test.py', encoding='utf-8') as f:
    print(f.read())

# 子目录中文件
with open('test1/test.txt', encoding='utf-8') as f:
    print(f.read())
