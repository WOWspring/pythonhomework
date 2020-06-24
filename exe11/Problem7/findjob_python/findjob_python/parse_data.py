#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 15:06
# @Author  : Ryu
# @Site    : 
# @File    : parse_data.py.py
# @Software: PyCharm


def count_salary(salary_text:str):
    date_radix = 1   #薪资基数
    unit_radix = 1   #单位基数
    avge = 0    #平均工资(无基数)
    wages = 0   #最终工资

    if salary_text[-1] == '天':
        avge = float(salary_text[:-3])
        date_radix = 365
        wages = avge * date_radix * unit_radix
        return wages
    else:
        wageslist = list(map(float, salary_text[:-3].split('-')))
        avge = sum(wageslist) / len(wageslist)
        if salary_text[-1] == '月':
            date_radix = 12
        if salary_text[-3] == '千':
            unit_radix = 1000
        elif salary_text[-3] == '万':
            unit_radix = 10000
        wages = avge * unit_radix * date_radix
        return wages


