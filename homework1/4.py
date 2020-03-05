# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/03/05 16:19:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question: 判断用户输入的年份是否为闰年
#闰年规则为， 四年一闰，百年不闰，四百年大闰
#注意类型转换，input返回的值是字符串类型的
JudgeYear = int(input("请输入想要判断是否为闰年的年份:"))
if JudgeYear % 4 == 0:
    if JudgeYear % 100 == 0 and JudgeYear % 400 != 0:
        print("不是闰年！")
    else:
        print("是闰年!")
else:
    print("不是闰年！")
    