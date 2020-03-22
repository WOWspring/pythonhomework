# -*- encoding: utf-8 -*-
'''
@File : func_def.py
@Time : 2020/03/22 10:22:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# functest

def cal(weight, price):
    return weight * price

weight, price = map(float, input("请输入苹果重量和单价: ").split())
print("总价格为:", cal(weight, price))
