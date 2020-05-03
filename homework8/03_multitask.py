# -*- encoding: utf-8 -*-
'''
@File : 03_multitask.py
@Time : 2020/05/01 15:03:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

from multiprocessing import Process, Queue
import functools
import datetime
from math import sqrt


Q = Queue()

def count_time():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            st = datetime.datetime.now()
            result = func(*args, **kw)
            et = datetime.datetime.now()
            number_process = 0
            if len(args) == 0:
                number_process = 1
            else:
                number_process = args[0]
            print('number of the process: {}, cost time = {}, end count is {}'.format(number_process, et - st, result))
        return wrapper
    return decorator


def judge_prime(m):
    for i in range(2, int(sqrt(m))+ 1):
        if m % i == 0:
            return 0
    else:
        return 1

#对比1
@count_time()
def non_count_prime():
    count1 = 0
    for i in range(1, 100001):
        count1 += judge_prime(i)
    return count1

def muti_judge_prime(julist, Q):
    count = 0
    for i in julist:
        count += judge_prime(i)
    Q.put(count)

@count_time()
def muti_count_prime(number):
    plist = []
    step = 100000 // number
    sum_count = 0
    for i in range(number):
        process = Process(target = muti_judge_prime, args = (range(i * step + 1, i * step + step), Q))
        plist.append(process)
        process.start()
    for p in plist:
        p.join()
    while not Q.empty():
        sum_count += Q.get()
    return sum_count

if __name__ == '__main__':
    print('compare with single process and multi processes')
    non_count_prime()
    muti_count_prime(2)
    print('compare with 4 processes and 10 processes')
    muti_count_prime(4)
    muti_count_prime(10)


# def multit_count_prime(startindex, step):
#     global count2
#     for i in range(startindex, startindex + 100000 // step):
#         count2 += judge_prime(i)

# @count_time()
# def count_multi_time(step):
#     global count2
#     for i in range(step):
#         p = Process(target = multit_count_prime, args = (i * 100000 // step + 1, step))
#         p.start()
#         p.join()

# if __name__ == '__main__':
#     print(count_prime)
#     print(count_multi_time(2))
