# -*- encoding: utf-8 -*-
'''
@File : fight.py
@Time : 2020/04/13 16:52:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

from people import peoplec as people
from dog import dogc as dog
import random
import time

class fight:
    '''
    fight规则， 随机数选择先攻的一方，哪边生命值全为0就判定胜负。
    '''
    stop = 0.1

    def __init__(self):
        p1 = people()
        p2 = people()
        d1 = dog()
        d2 = dog()
        d3 = dog()
        self.PList = [p1, p2]
        self.DList = [d1, d2, d3]

    def __setflag(self):
        #随机选择谁先攻击
        self.__flag = random.randint(0, 1)
    
    def __changeflag(self):
        #攻击轮换
        if self.__flag == 0 :
            self.__flag = 1
        else:
            self.__flag = 0

    def __judge(self):
        '''
        用于判断胜负
        死了就从列表中剔除
        '''
        if len(self.PList) == 0:
            return 1
        elif len(self.DList) == 0:
            return -1
        else:
            return 0

    def combat(self):
        self.__setflag()

        while(self.__judge() == 0):
            if self.__flag == 0:
                #0为人类攻击
                print('轮到人类进攻！')
                time.sleep(self.stop)
                #最好能列举一下人类情况
                #attackindex = int(input('请安排发起进攻的人(您可以选择0-{}):'.format(len(self.PList))))
                attackindex = random.randint(0, len(self.PList) - 1)
                targetindex = random.randint(0, len(self.DList) - 1)
                self.DList[targetindex].dbitetd(self.PList[attackindex].attack) #随机的狗狗被安排的人进攻
                print('人类{}号对狗狗{}号发起了进攻！'.format(attackindex, targetindex))
                time.sleep(self.stop)
                if self.DList[targetindex].life > 0:
                    print('狗狗{}号受到了{}点伤害！还剩{}血！'.format(targetindex, self.PList[attackindex].attack, self.DList[targetindex].life))
                    time.sleep(self.stop)
                    print('狗狗{}号的攻击力降低了！只有{}点攻击力了！'.format(targetindex, self.DList[targetindex].attack))
                    #error这两句话应当放到条件语句当中
                else:
                    print('狗狗{}号血量降至0以下了！狗狗{}号阵亡了！'.format(targetindex, targetindex))
                    del self.DList[targetindex]
                time.sleep(self.stop)
                self.__changeflag()
            else:
                #1为狗狗攻击
                print('轮到狗狗进攻！')
                time.sleep(self.stop)
                #attackindex = int(input('请安排发起进攻的人(您可以选择0-{}):'.format(len(self.PList))))
                attackindex = random.randint(0, len(self.DList) - 1)
                targetindex = random.randint(0, len(self.PList) - 1)
                self.PList[targetindex].pbitetd(self.DList[attackindex].attack) 
                print('狗狗{}号对人类{}号发起了进攻！'.format(attackindex, targetindex))
                time.sleep(self.stop)
                if self.PList[targetindex].life > 0:
                    print('人类{}号受到了{}点伤害！还剩{}血！'.format(targetindex, self.DList[attackindex].attack, self.PList[targetindex].life))
                    time.sleep(self.stop)
                    print('人类{}号的攻击力降低了！只有{}点攻击力了！'.format(targetindex, self.PList[targetindex].attack))                
                else:
                    print('人类{}号血量降至0以下了！人类{}号阵亡了！'.format(targetindex, targetindex))
                    del self.PList[targetindex]
                time.sleep(self.stop)
                self.__changeflag()
        else:
            if self.__judge() == 1:
                print('狗狗获得了胜利！人类一败涂地！')
            else:
                print('人类光荣获胜！狗狗终是畜生！')

F1 = fight()
F1.combat()