# -*- encoding: utf-8 -*-
'''
@File : 04_count.py
@Time : 2020/03/13 22:52:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def count(a):
    alpha = 0  #记录字母
    figure = 0  #记录数字
    space = 0  #记录空格
    others = 0  #记录其他字符
    for i in range(len(a)):
        if a[i].isalpha():
            alpha += 1
        elif a[i].isdigit():
            figure += 1
        elif a[i].isspace():
            space += 1
        else:
            others += 1
    print(f"alpha: {alpha}\nfigure: {figure}\nspace: {space}\nothers: {others}")
        



text = "Youth means a temperamental predominance of courage over timidity , of the appetite for adventure over the love of ease . This often exits in a man of 60 , more than a boy of 20 .nobody grows merely by the number of years ; we grow old by deserting our ideas . Years may wrinkle the skin , but to give up enthusiasm wrinkles the soul . Worry , fear , self-distrust1 bows the heart and turns the spirit back to dust ."
count(text)