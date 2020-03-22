# -*- encoding: utf-8 -*-
'''
@File : pass_by_ref.py
@Time : 2020/03/22 10:26:00
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#研究python中变量名的实际含义
# 考察Python函数参数传递
def change(a):
    print("调用函数时形参列表修改前:", a)
    a.extend([1, 3, 5])
    print("调用函数时形参列表修改后:", a)
    print("调用函数时形参列表地址:", id(a))


b = [1, 2, 3]
print("未调用函数时的列表地址:", id(b))
change(b)
print("调用函数后列表内容: ", b)
print("调用函数后列表地址:", id(b))
