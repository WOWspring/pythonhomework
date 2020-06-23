#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 21:16
# @Author  : Ryu
# @Site    : 
# @File    : start.py.py
# @Software: PyCharm

from scrapy import cmdline
from urllib.parse import quote
print(quote('python开发工程师'))
# cmdline.execute('scrapy crawl findjob'.split())
# cmdline.execute('scrapy crawl findjob -s LOG_FILE=all.log'.split())