# -*- encoding: utf-8 -*-
'''
@File : 06_Conduct_Entxt.py
@Time : 2020/03/23 22:59:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
# 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#     比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);

#注意清除标点之后再统计
import re
import os
 
#字符串处理函数，去除标点符号 
punctuation = '!,;:?"\'-().>'      #在符号中加了_后会出现吞大写字母的问题，不知道为什么
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)     #正则表达式处理
    return text.strip().lower()
 
#利用homework1的countword来统计
# mydict = {word: sentence.split().count(word) for word in set(sentence.split())}   上课讲解的方法
def counttxt(text, frequencedict):
    textlist = text.split()
    for i in range(len(textlist)):
        if textlist[i] in frequencedict.keys():
            frequencedict[textlist[i]] += 1
        else:
            frequencedict[textlist[i]] = 1 
    return

#切换至当前目录
try:
    os.chdir("homework3")
except FileNotFoundError as fnf_error:
    print(fnf_error)


dict1 = {}
try:
    with open("Pythontxt1.txt", 'r', encoding = 'utf-8') as f:
        temp = f.readline()
        while len(temp) > 0:
            #print(temp)
            #print(removePunctuation(temp))
            counttxt(removePunctuation(temp), dict1)           #先数据清洗，然后再统计
            temp = f.readline()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')
#排序
sorteddict1 = sorted(dict1.items(), key = lambda x : x[1], reverse = True )#sorted函数返回的是元组形式的列表
#写入文件
try:
    with open("sortpt1.txt", 'w', encoding = 'utf-8') as f:
        for t in sorteddict1:
            f.write(f"{t}" + '\n')
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')

dict2 = {}
try:
    with open("Pythontxt2.txt", 'r', encoding = 'utf-8') as f:
        temp = f.readline()
        while len(temp) > 0:
            counttxt(removePunctuation(temp), dict2)           #先数据清洗，然后再统计
            temp = f.readline()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')

#排序
sorteddict2 = sorted(dict2.items(), key = lambda x : x[1], reverse = True )#sorted函数返回的是元组形式的列表
#写入文件
try:
    with open("sortpt2.txt", 'w', encoding = 'utf-8') as f:
        for t in sorteddict2:
            f.write(f"{t}" + '\n')
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')

#取出各个排序列表中的前十个做成集合
set1 = {x[0] for x in sorteddict1[0:10]}
set2 = {x[0] for x in sorteddict2[0:10]}
# print(set1)
# print(set2)
#两集合合并，少了几个元素就是几个相同
sumset = set1 | set2
sim = (20 - len(sumset)) * 10
print(f"相似度为{sim}%")