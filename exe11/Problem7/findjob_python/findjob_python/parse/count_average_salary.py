#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 19:50
# @Author  : Ryu
# @Site    : 
# @File    : count_average_salary.py.py
# @Software: PyCharm


def count_average_salary(search_targrt='北京'):
    """

    Returns:
        Calculate the salary level of Beijing area based on the file of crawling data.
    """
    sum_salary = 0.00
    target_count = 0
    count = 0
    with open('../data/JobInfo.txt', 'r', encoding='gbk') as f:
        temp = f.readline().strip()
        while len(temp) != 0:
            print('\r当前计算进度：{}/{}'.format(target_count, count), end='')
            count = count + 1
            if search_targrt in temp:
                temp_list = temp.split()
                target_count = target_count + 1
                if float(temp_list[3]) != 0:
                    sum_salary = sum_salary + float(temp_list[3])
            temp = f.readline().strip()
        if count == 0:
            print('城市输入错误或者该城市没有该工作需求。')
            return 0
    return sum_salary / target_count


if __name__ == '__main__':
    print('=' * 30)
    print('\n北京的Python开发工程师的平均薪资为{:.2f}元/年'.format(count_average_salary()))
    print('='*30)
    while True:
        temp = input('您还可以选择其他城市进行计算或者输入0退出：')
        if temp == '0':
            exit(1)
        else:
            print('=' * 30)
            print('\n{}的Python开发工程师的平均薪资为{:.2f}元/年'.format(temp, count_average_salary(search_targrt=temp)))
            print('=' * 30)