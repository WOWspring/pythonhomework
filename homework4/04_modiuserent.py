# -*- encoding: utf-8 -*-
'''
@File : 04_modiuserent.py
@Time : 2020/03/27 16:08:33
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
# 系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
import hashlib

namelist = []
accountlist = []
passwordlist = []
with open('userinfo.txt', 'r', encoding = 'utf-8') as f:
    info = f.readlines()
    for x in info:
        x.strip('\n')   #去除换行
        temp = x.split()
        namelist.append(temp[0])
        accountlist.append(temp[1])
        passwordlist.append(temp[2])
    
name = input('请输入同学的名字:')
if name in namelist:
    flag = namelist.index(name)
    account = input('请输入该同学的账号:')
    if account == accountlist[flag]:
        password = input('请输入该同学该账号的密码：')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        pwd = md5.hexdigest()
        if pwd == passwordlist[flag]:
            print('登录成功！')
        else:
            print('密码错误！')
    else:
        print('该同学的账号不是这个！')

else:
    print('没有该同学的名字！')

