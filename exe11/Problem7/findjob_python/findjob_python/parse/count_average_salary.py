#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 19:50
# @Author  : Ryu
# @Site    : 
# @File    : count_average_salary.py.py
# @Software: PyCharm


def count_average_salary():
    """

    Returns:
        Calculate the salary level of Beijing area based on the file of crawling data.
    """
    sum_salary = 0.00
    count = 0
    with open('../data/JobInfo.txt', 'r') as f:
        temp = f.readline().strip()
        while len(temp) != 0:
            print('\r当前计算进度：{}'.format(count), end='')
            if '北京' in temp:
                temp_list = temp.split()
                count = count + 1
                sum_salary = sum_salary + float(temp_list[3])
            temp = f.readline().strip()
    return sum_salary / count


if __name__ == '__main__':
    print('=' * 30)
    print('\n北京的Python开发工程师的平均薪资为{}'.format(count_average_salary()))
    print('='*30)