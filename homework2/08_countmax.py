# -*- encoding: utf-8 -*-
'''
@File : 08_countmax.py
@Time : 2020/03/13 23:47:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
from collections import  Counter

def getmax(t):
    return Counter(t).most_common(1)

text = "Youth means a temperamental predominance of courage over timidity , of the appetite for adventure over the love of ease . This often exits in a man of 60 , more than a boy of 20 .nobody grows merely by the number of years ; we grow old by deserting our ideas . Years may wrinkle the skin , but to give up enthusiasm wrinkles the soul . Worry , fear , self-distrust1 bows the heart and turns the spirit back to dust ."
#print(getmax(text)[0][1])
print(f"最多的字符是：\'{getmax(text)[0][0]}\', 共有{getmax(text)[0][1]}个")