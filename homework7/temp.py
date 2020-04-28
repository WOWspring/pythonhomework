# -*- encoding: utf-8 -*-
'''
@File : 02_urlspider.py
@Time : 2020/04/22 20:24:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#  给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库

import os
import urllib.request as urllib2

#http不采用持久连接
hh = { 
    "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    'Connection':'close'
    }
data = None


try:
    os.chdir('pythonhomework\homework7')
except FileNotFoundError as identifier:
    print(identifier)


with open('urlspider.txt', 'w', encoding = 'utf-8') as f:
        re = urllib2.Request(r'http://www.kbstarchina.com', data, hh)
        r = urllib2.urlopen(re)
        html = r.read()
        f.write(str(html, encoding = 'utf-8'))  

