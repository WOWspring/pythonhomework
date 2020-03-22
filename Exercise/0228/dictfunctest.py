# -*- encoding: utf-8 -*-
'''
@File : dictModify.py
@Time : 2020/03/20 22:23:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 定义字典，并对字典进行增删改操作
info = {
    'number': '120181080223',
    'name': '姚鹏飞',
    'class': '软件1801',
    'age': 20
}

info['sex'] = 'man'  # 添加元素
info['age'] = 21  # 修改元素
del info['number']  # 删除键值对
print(info)
