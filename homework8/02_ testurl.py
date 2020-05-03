# -*- encoding: utf-8 -*-
'''
@File : 02_ testurl.py
@Time : 2020/05/01 10:29:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"
#   数据文件（1000个网址）：

import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    os.chdir('pythonhomework\homework8')
except FileNotFoundError as fnf_err:
    print(fnf_err)

step = 100 #步长

#先读入文本
url_data_list = []
#保存结果
test_list = [] 

with open('url_data.txt', 'r', encoding = 'gbk') as file:   # utf-8会存在解码错误的问题，改用gbk读取
    url_data_list = file.readlines()
#去回车
url_data_list = [t.strip('\n') for t in url_data_list]

def getHtmlText(url):
    #只需要是否可以访问的结论就可以了
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        # r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        # r.encoding = r.apparent_encoding
        # return r.text
        return "正常访问"
    except:
        return "产生异常"

def test_url(startindex):
    for t in url_data_list[startindex : startindex + step]:
        target = getHtmlText(t)
        test_list.append(f'{t} : {target}') 
        print(f'{t} : {target}')

if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    all_task = [pool.submit(test_url, i * 100) for i in range(10)]

    for t in as_completed(all_task):
        t.result()