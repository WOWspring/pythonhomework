# -*- encoding: utf-8 -*-
'''
@File : 03_wegt.py
@Time : 2020/04/29 15:12:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
#      这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

#    要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
#   Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
# 注意：
# 获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
# MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
# >>> from urllib.parse import quote
# >>> quote('2019-04-13 NEWSworthy Clips.mp3')
# '2019-04-13%20NEWSworthy%20Clips.mp3'

'''
题目是错的，有sc-ad， 不能url编码
'''

import re
import os
import requests
from bs4 import BeautifulSoup
import lxml
from urllib.parse import quote
import wget

try:
    os.chdir(r'pythonhomework\homework7')
except FileNotFoundError as identifier:
    print(identifier)


with open('wget.txt', 'w', encoding = 'utf-8') as f:
    url = r'http://www.listeningexpress.com/studioclassroom/ad/'
    html = requests.get(url).text
    f.write(html)

text = []
with open('wget.txt', 'r', encoding = 'utf-8') as f:
    #不能用beautifulsoup筛选，因为留下的文本是网页上显示的，不是所需要的连接
    # html = f.read()
    # bs_get = BeautifulSoup(html, 'lxml')
    # text = bs_get.find_all(text = True)
    text = f.readlines()
    # for t in text:
    #     print(t)


#html文本处理,文本清洗
# print('-------------------------------------------------------------------')
# text = set(text)
# print(text)
retext = r'sc-ad.*\.mp3'
anoretext = r'sc-ad.{20,40}\.mp3'
relist = []

# for t in text:
#     pipei = re.search(retext, t)
#     if pipei:
#         relist.append("http://www.listeningexpress.com/studioclassroom/ad/" + quote(pipei.group()[5 : ]))  #url编码,合并网址
#网址存在问题因此要重新修改正则匹配
for t in text:
    pipei = re.search(retext, t)
    if pipei:
        relist.append(pipei.group())
# print(relist)
#清洗文本
relist = re.findall(anoretext, relist[0])
for i,k in enumerate(relist):
    relist[i] = "http://www.listeningexpress.com/studioclassroom/ad/" + k  #sc-ad 也是不要的
    print(relist[i])

try:
    os.chdir(r'.\mp3download')
except FileNotFoundError as identifier:
    print(identifier)

for t in relist:
    wget.download(t)
