# -*- encoding: utf-8 -*-
'''
@File : while_if_statement.py
@Time : 2020/03/22 10:21:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 遍历输出列表中的偶数
a = [1,2,5,4,8,7,6,8,4,14,1,4,55,2,1,3,6,4,9]
print("输出列表:", a)
for i in a:
    if i % 2 == 0:
        print(i, end=' ')
