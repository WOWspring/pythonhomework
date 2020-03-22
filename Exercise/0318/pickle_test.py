# -*- encoding: utf-8 -*-
'''
@File : pickle_test.py
@Time : 2020/03/22 10:51:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习5 使用pickle模块序列化对象
# 给定一个字典，保存了5个同学的学号、姓名、年龄
# 使用pickle模块将数据对象保存到文件中去

import os
import pickle

infos = [
    {'学号': '01', 'name': '张三', 'age': 14},
    {'学号': '03', 'name': '李四', 'age': 29},
    {'学号': '05', 'name': '赵武', 'age': 57},
    {'学号': '06', 'name': '彩六', 'age': 12},
    {'学号': '08', 'name': '王八', 'age': 80}
]

os.chdir('Exercise/0318')
# 二进制保存
with open('infos', 'wb') as f:
    pickle.dump(infos, f)

# 二进制读取
with open('infos', 'rb') as f:
    load_infos = pickle.load(f)
    print(load_infos)
