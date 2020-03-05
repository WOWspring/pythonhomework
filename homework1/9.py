# -*- encoding: utf-8 -*-
'''
@File : 9.py
@Time : 2020/03/05 18:04:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question: 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

import random

#提示用户选择N和数字的大小规模：
#input返回一个字符串， split按照空格拆开， map把迭代序列转换数据类型
N, maxnumber = map(int, input("请输入想要猜的次数以及所猜数字的区间是从1到多大？：").split())    
#print(type(maxnumber))   神奇的错误！在注释符号之前，如果是和代码同行的话，不要有中文的空格，会报SyntaxError: invalid character in identifier的错误
targetnumber = random.randint(1,maxnumber) #所要猜的目标数字
# print(targetnumber)
# print(type(targetnumber))

for i in range(N):
    trynumber = int(input("请输入您猜的数字:"))  #不要忘记转换类型
    # print(trynumber)
    # print(type(trynumber))
    if trynumber == targetnumber:
        print(f"恭喜你！猜了{i+1}次猜对了！")
        break
    elif trynumber > targetnumber:  #注意不要打错。。
        print("实际上的数字比这个小哦，继续努力！")
    else:
        print("实际上的数字比这个大哦，继续努力！")
else:
    print("次数用完了！失败……")