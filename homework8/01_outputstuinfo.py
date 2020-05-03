# -*- encoding: utf-8 -*-
'''
@File : 01_outputstuinfo.py
@Time : 2020/04/30 22:16:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；

import threading
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
# from future import ThreadPoolExecutor, as_completed
stuinfo = [random.randint(0,100) for x in range(100)]

# A方法
class out_stu(threading.Thread):
    def __init__(self, start_index, end_index):
        #注意继承，否则初始化会失败
        threading.Thread.__init__(self) 
        self.start_index = start_index
        self.end_index = end_index

    def run(self):
        for i in range(self.start_index, self.end_index):
            print(stuinfo[i])

if __name__ == "__main__":
    for i in range(0,5):
        t = out_stu(i * 20, i * 20 + 20)
        t.start()

# B方法, 线程池

# def out_stu(start_index, end_index):
#     for i in range(start_index, end_index):
#         print(stuinfo[i])


# if __name__ == "__main__":
#     pool = ThreadPoolExecutor(3)
#     all_task = [pool.submit(out_stu, i * 20 ,i * 20 + 20) for i in range(5)]        #参数不需要包装成元组，直接一个一个打进去就行

#     for future in as_completed(all_task):
#         future.result() 

