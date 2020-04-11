# -*- encoding: utf-8 -*-
'''
@File : 03_decap.py
@Time : 2020/04/11 14:58:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

import os
import functools

try:
    os.chdir('pythonhomework\homework5')
except FileNotFoundError as identifier:
    print(identifier)

def judgeap(inputa, tara, inputp, tarp):
    '''
    用于判断输入的账号密码和文档中保存的账号密码是否匹配
    '''
    if inputa == tara and inputp == tarp:
        return True
    else:
        return False

def identify():
    '''
    装饰器，用于权限认证
    '''
    def decorater(func):
        @functools.wraps(func)
        def wrapper(*args, **kws):
            print('您正在试图访问{}函数，该函数的调用需要权限认证。'.format(func.__name__))
            with open('account&passw.txt', 'r', encoding = 'utf-8') as f:
                account = input('请输入账户:')
                password = input('请输入密码：')
                temp = f.readline().strip('\n').split()
                while not judgeap(account, temp[0], password, temp[1]):
                    temp = f.readline().strip('\n').split()
                    if len(temp) == 0 :
                        print('账号密码匹配失败！您无权限调用函数')
                        return    #用break的话还需要处理函数调用跑出的异常，直接return应该会更好
                else:
                    print('权限认证成功！')
                    result = func(*args, **kws)
                    print(result)
            return result
        return wrapper
    return decorater

@identify()
def plus(a, b):
    return a + b

plus(1,2)



                
