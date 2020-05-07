# -*- encoding: utf-8 -*-
'''
@File : get_time.py
@Time : 2020/05/06 20:26:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import datetime

def get_time():
    time = datetime.datetime.now()
    conduct_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return conduct_time