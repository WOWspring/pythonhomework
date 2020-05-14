# -*- encoding: utf-8 -*-
'''
@File : 04_htmldown.py
@Time : 2020/05/13 16:01:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
#     文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

#   参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
#    大家看完这篇文档后，再开始动手做这道题；

from bs4 import BeautifulSoup
import requests
import os

count = 0

try:
    os.chdir('pythonhomework\homework7')
except FileNotFoundError as identifier:
    print(identifier)

url = r'https://www.programcreek.com/python/index/221/requests'

headers = { 
    "User-Agent" : 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    #'Connection':'close'
    'content-type': 'text/html'
    }

def clone_test(url):
    global count
    count += 1
    print('Cloning test{}……'.format(count))
    try:
        temp = requests.get(url, headers = headers, timeout = 10).text     
    except:
        pass   

    temp_soup = BeautifulSoup(temp, 'lxml')
    lk = temp_soup.find_all('pre', class_ = 'prettyprint')  #为什么要加一个_      class是python的保留字，所以需要用class_来代替
    test_title = temp_soup.title.string
    if len(lk) == 0:
        print('This page has no code, skip……')
        return
    # print(test_title)
    # print(type(test_title))
    # for v in lk:
    #     print(v.string)
    with open('requests_code.txt', 'a', encoding = 'utf-8') as f:
        f.write('*' * 15 + test_title + '*' * 15 + '\n')
        for k, v in enumerate(lk):
            #去空防止报错
            # print(v.string)
            if v.string is None:
                continue
            f.write(f'Example {k + 1}:\n')
            f.write(v.string + '\n')
            f.write('*' * 30 + '\n')
        f.write('\n')
        print('Successfully cloned the example code to requests_code.txt!')



data = None

linkset = set()
try:
    result = requests.get(url, headers = headers, timeout = 30).content.decode('utf-8')
    soup = BeautifulSoup(result, 'lxml')
    linklist = soup.find('ul', id = 'api-list').find_all('a', href = True)
    # print(linklist)
    
    for l in linklist:
        # print(type(l))
        # print(l.attrs['href'])
        linkset.add(l.attrs['href'])
except Exception as identifier:
    print(identifier)

for v in linkset:
    clone_test(v)
print('all done')