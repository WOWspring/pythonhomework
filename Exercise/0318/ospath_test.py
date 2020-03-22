# -*- encoding: utf-8 -*-
'''
@File : os_path_test.py
@Time : 2020/03/22 10:46:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习1 使用os.path模块下函数的使用
import os

# 打印文件名
print(os.path.basename(r'D:\gitwork\pythonhomework\homework1\01_findnum.py'))
# 打印路径名
print(os.path.dirname(r'D:\gitwork\pythonhomework\homework1\01_findnum.py'))
# 分隔路径名和文件名
print(os.path.split(r'D:\gitwork\pythonhomework\homework1\01_findnum.py'))
# 拼接路径
print(os.path.join(r'D:\gitwork', 'pythonhomework\homework1\01_findnum.py'))
