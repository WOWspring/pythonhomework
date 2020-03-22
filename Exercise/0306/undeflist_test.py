# -*- encoding: utf-8 -*-
'''
@File : var_args.py
@Time : 2020/03/22 10:29:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 不定长参数练习
def undeflist(*args):
    # 封装成列表
    print(list(args))
    # 封装成字典
    print({i: v for i, v in enumerate(args)})


undeflist(6, 8, 4, "WOW", False)
