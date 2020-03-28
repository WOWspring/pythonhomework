# -*- encoding: utf-8 -*-
'''
@File : 03_actpwd2file.py
@Time : 2020/03/27 15:03:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX   

#采用MD5摘要算法

import hashlib
import os

with open('userinfo.txt', 'w', encoding = 'utf-8') as f:
    for i in range(5):
        name, account, password = input(f"请输入第{i + 1}个同学的姓名、账号和密码:").split()
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))        #hash之前需要编码
        pwdplus = md5.hexdigest()
        f.writelines(f'{name}\t{account}\t{pwdplus}\n')
