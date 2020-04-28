# -*- encoding: utf-8 -*-
'''
@File : 01_email.py
@Time : 2020/04/15 09:09:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com

import re

def judge(mail):
    ret = re.match(r"^[a-zA-Z0-9]{4,20}@163\.com$", mail)
    if ret:
        print("输入正确")
    else:
        print('输入错误！')

if __name__ == "__main__":
    judge(input('请输入您的邮箱：'))