#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 9:33
# @Author  : Ryu
# @Site    : 
# @File    : bs4test.py.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import bs4

soup = BeautifulSoup(open('JobInfo.txt'), "html.parser")
jobskim = soup.find_all('div', class_='dw_table', id="resultList")[0]
jobskim: bs4.element.Tag
jobInfo = jobskim.find_all('div', class_='el')[1:]
print(jobskim)
print(type(jobskim))
print(jobInfo)
print(type(jobInfo))