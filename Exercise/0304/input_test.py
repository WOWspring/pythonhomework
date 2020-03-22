# -*- encoding: utf-8 -*-
'''
@File : input.py
@Time : 2020/03/20 22:34:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# input()函数实验
# 根据空格分割后转换成元组，尝试使用split
msg = input("请输入字符串: ")
temp = tuple(msg.split())
print(temp)

weight = float(input("请输入购买苹果的重量: "))
price = float(input("请输入苹果的单价: "))
print("总价为%d元" % (weight * price))
