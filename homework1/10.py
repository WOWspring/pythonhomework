# -*- encoding: utf-8 -*-
'''
@File : 10.py
@Time : 2020/03/05 20:33:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question: 10  给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#    提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#     先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 
#     如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 
#     如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；
text = "Youth means a temperamental predominance of courage over timidity , of the appetite for adventure over the love of ease . This often exits in a man of 60 , more than a boy of 20 .nobody grows merely by the number of years ; we grow old by deserting our ideas . Years may wrinkle the skin , but to give up enthusiasm wrinkles the soul . Worry , fear , self-distrust1 bows the heart and turns the spirit back to dust ."
textlist = text.split()

frequencedict = {}
#统计,包括标点
for i in range(len(textlist)):
    if textlist[i] in frequencedict.keys():
        frequencedict[textlist[i]] += 1
    else:
        frequencedict[textlist[i]] = 1 
#排序
sortedfrdict = sorted(frequencedict.items(), key = lambda x : x[1], reverse = True )#sorted函数返回的是元组形式的列表

for i in range(len(sortedfrdict)):
    print(f"{sortedfrdict[i][0]}: {sortedfrdict[i][1]}") 