# -*- encoding: utf-8 -*-
'''
@File : string_format.py
@Time : 2020/03/21 22:27:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 测试多种拼接、格式化字符串的方式
# test code snippet #1
rootnumber = input('rootnumber: ')
rootpwd = input('rootpwd: ')
print(rootnumber, rootpwd)

# test code snippet #2.1
number = input("number: ")
sex = input("sex: ")
name = input("name: ")
capital = input("capital:")
baseinfo = '  baseinfo of ' + number + ' number: ' + number + ' sex: ' + sex + ' name: ' + name + ' capital: ' + capital + ' '
print(baseinfo)

# test code snippet #2.2
number = input("number: ")
sex = input("sex: ")
name = input("name: ") 
capital = input("capital: ")
baseinfo1 = '  baseinfo of %s --- number:%s sex:%s name:%s capital:%s ' % (number, number, sex, name, capital)
print(baseinfo1)

# test code snippet #3
number = input("rootnumber：")
sex = input("sex：")
name = input("name：")
capital = input("capital：")
# 此处是赋值
baseinfo = '  baseinfo of {_number} number：{_number} sex：{_sex} name：{_name} capital：{_capital} '.format(_number=number, _sex=sex, _name=name, _capital=capital)
print(baseinfo)

# test code snippet #4
number = input("number：")
sex = input("sex：")
name = input("name：")
capital = input("capital：")
baseinfo = '  baseinfo of {0}--- number：{0} sex：{1} name：{2} capital：{3} '.format(number, sex, name, capital)
print(baseinfo)