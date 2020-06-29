#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020/6/21 21:15
#  @Author  : Ryu
#  @Site    :
#  @File    : taobao_goods.py.py
#  @Software: PyCharm

import requests
import re


def getHTMLTest(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding        #apparent可以手动分析，节省时间
        return r.text
    except:
        return ''


def parsePage(ilt, html):
     try:
         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
         tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
         for i in range(lne(plt)):
             price = eval(plt[i].split(':')[1])
             title = eval(tlt[i].split(':')[1])
             ilt.append([price, title])
     except:        #不会因为一些错误而退出，更加稳定
         print("")


def printGoodList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '溜溜球'
    start_url = 'https://s.taobao.com/search?q=' + goods
    depth = 3
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLTest(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodList(infolist)


if __name__ == '__main__':
    main()
