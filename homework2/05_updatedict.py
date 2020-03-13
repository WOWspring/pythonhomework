# -*- encoding: utf-8 -*-
'''
@File : 05_updatedict.py
@Time : 2020/03/13 23:02:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def updatedict(d):
    for k,v in d.items():
        if len(v) > 2:
            temp = v[1:3]
            d[k] = temp

mydict = {
    'tuple1' : (1,4,5),
    'tuple2' : (1,2,4,5),
    'tuple3' : (5,),
    'tuple4' : (3,5,8),
    'tuple5' : (1,2),
    'tuple6' : (6,5,8,7,4,9,8),
    'tuple7' : (3,)   
}

print(f"原字典为:{mydict}")
updatedict(mydict)
print(f"更新后的字典为:{mydict}")