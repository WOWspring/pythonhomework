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

import requests
from bs4 import BeautifulSoup
import os
import lxml
import time
import urllib.request as urllib2

#爬取下来的网页中有些无法访问，有些会有反爬取，删减掉了一些，所以用的是temp.txt而不是之前生成的newUrl.txt
#网站编码有问题的用gbk
#http不采用持久连接
#UA伪装成chorme
# headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# hh = { 
#     "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
#     'Connection':'close'
#     }

'''
按照题干要求的爬取结果（没有匹配简介）
['http://www.chrtc.cn', 'http://www.chrtc.cn', 'http://www.chrtc.cn', 'http://www.chrtc.cn', 'http://www.chrtc.cn', '网页读取异常，跳过！', 'http://www.fscinda.com', 'http://www.fscinda.com', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', 'http://www.sdictrade.com', 'http://www.sdictrade.com', '网页读取异常，跳过！', 'http://www.airchinacargo.com', '网页读取异常，跳过！', 'http://www.cytsonline.com', '网页读取异常，跳
过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', 'http://www.cnfuelco.com', 'http://www.cnfuelco.com', 'http://www.cnfuelco.com', 'http://www.cahic.com', 'http://www.bocim.com', 'http://www.cercg.com', '网页读取异常，跳
过！', 'http://www.zddkjs.com', 'http://www.zddkjs.com', '网页读取异常，跳过！', 'http://www.chnphoto.cn', '网页读取异常，跳过！', '网页读取异常，跳
过！', 'http://www.dfac.com', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！', '网页读取异常，跳过！']
'''

hh = { 
    "User-Agent" : 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Connection':'close'
    }
data = None

c = 1
composelist = []
def judgeurl(urlw):
    global c
    #每次把网页爬取到文本文档时都覆盖之前的内容
    with open('urlspider.txt', 'w', encoding = 'utf-8') as f:
        try:
            print(urlw)
            c += 1
            re = urllib2.Request(urlw, data, hh)
            r = urllib2.urlopen(re)
            html = r.read()
            f.write(str(html, encoding = 'utf-8'))  
        # except http_client.IncompleteRead as e:
        #     #处理不完整读取异常
        #     buffer = e.partial
        # except Exception as identifier:
        #     raise(Exception)
        except Exception as ex:
            #尝试，有错跳过不处理
            print('网页读取异常，跳过！')
            composelist.append('网页读取异常，跳过！')




    with open('urlspider.txt', 'rb') as f:
        txt = f.read()
        bs = BeautifulSoup(txt,"lxml")
        # print(bs)
        text = bs.find_all(text = True)
        # print(text)
        for t in text:
            if t in target_txt_list:
                composelist.append(urlw)
        

try:
    os.chdir('pythonhomework\homework7')
except FileNotFoundError as identifier:
    print(identifier)

target_txt_list = ['企业介绍', '关于我们', '企业发展', '发展历史', '企业概况', '公司介绍', '简介']

urllist = []    #将newUrl中的网址读到一个列表中
with open('temp.txt', 'r', encoding = 'utf-8') as f:
    temp = f.readline().strip('\n')
    count = 0 
    #超过100个会导致链接过多过频繁而报错
    while len(temp) > 0 and count < 100:
        urllist.append(temp)
        temp = f.readline().strip('\n')
        count += 1

for u in urllist:
    judgeurl(u)

# judgeurl(urllist[0])
print(composelist)
#print(urllist)

# with open('urlspider.txt', 'a+', encoding = 'utf-8') as f:
#     url = r'http://www.chrtc.cn/about.html'
#     re = requests.get(url)
#     ret = re.text
#     f.write(ret)

# with open('urlspider.txt', 'rb') as f:
#     txt = f.read()
#     bs = BeautifulSoup(txt,"lxml")
#     # print(bs)
#     text = bs.find_all(text = True)
#     print(text)

