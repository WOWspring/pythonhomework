#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 16:15
# @Author  : Ryu
# @Site    : 
# @File    : start.py.py
# @Software: PyCharm

from scrapy import cmdline
cmdline.execute("scrapy crawl SearchCompanyInfo".split())