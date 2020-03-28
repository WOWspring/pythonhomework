# -*- encoding: utf-8 -*-
'''
@File : 02_judgeweek.py
@Time : 2020/03/27 14:22:00
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
# 将程序改写一下，能针对我们学校的校历时间进行计算
# （ 校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

import datetime

def legal_date(year, month, day):
    '''判断输入的年月日是否合法
    input:year, month, day 
    output: boolean
    '''
    #利用homework1的闰年脚本
    #JudgeYear = int(input("请输入想要判断是否为闰年的年份:"))
    flag = 0        #记录是否是闰年
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            pass
        else:
            flag = 1
    else:
        pass
    if month in [1,3,5,7,9,11]:
        if day <= 31 and day >= 1:
            return True
        else :
            return False
    elif month in [4,6,8,10,12]:
        if day <= 30 and day >= 1:
            return True
        else:
            return False
    elif month == 2:
        if flag == 1:
            if day >= 1 and day <= 29:
                return True
            else:
                return False
        else:
            if day >= 1 and day <= 28:
                return True
            else:
                return False
    else:
        return False

def judgeweek(year, month, day):
    '''判断是第几周星期几：
    input: year, month, day
    output:numw(第几周), weekday(星期几)
    '''
    if legal_date(year, month, day):
        dt = datetime.date(year, month, day)
        wt = datetime.date(year, 1, 1)
        dletad = (dt - wt).days
        numw = dletad // 7 + 1
        print(f"{dt} 是{year}年的第{numw}个礼拜的星期{dt.weekday() + 1}")     #似乎是老python的版本，星期几是需要加一的
    else:
        print("日期输入有误！不存在这个日期！")

def judgeschweek(year, month, day):
    '''判断是校历的第几周星期几：
    input: year, month, day
    output:numw(第几周), weekday(星期几)
    '''
    if legal_date(year, month, day):
        dt = datetime.date(year, month, day)
        bin_schdt = datetime.date(2020, 2 ,17)
        end_schdt = datetime.date(2020, 8, 23)
        if (dt - bin_schdt).days >= 0 and (dt - end_schdt).days <= 0:
            dletad =  (dt - bin_schdt).days
            numw = dletad // 7 + 1
            print(f"{dt} 是{year}年的校历第{numw}周的星期{dt.weekday() + 1}")
        else:
            print("该日期不在校历内！")
    else:
        print("日期输入有误！不存在这个日期！")

year, month, day = map(int, input("请输入年月日：").split())
judgeweek(year, month, day)
judgeschweek(year, month, day)