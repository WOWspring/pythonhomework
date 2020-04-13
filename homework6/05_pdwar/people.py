# -*- encoding: utf-8 -*-
'''
@File : people.py
@Time : 2020/04/13 16:07:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class peoplec:
    # SURlist = []    #用于保存堆栈的人
    '''
    人类，初始化方法会新置血量，攻击力
    被咬后会降低血量和攻击力，并且刷新生命状态和攻击状态
    '''
    def __init__(self):
        self.attack = 10
        self.life = 100
        self.status = True  #True means alive, False means dead
        #self.fesibattc = True   #True means still can fight, False means cannot combat
        # people.SURlist.append(self)
    
    def pbitetd(self, damage):
        #Being bitetd will decrease 2 attack and resume life equals to damage
        if damage != 0:
            if self.attack != 0:
                self.attack -= 2
        self.life -= damage
        if self.life <= 0:
            self.status = False
        # if self.attack <= 0:
        #     self.fesibattc = False
   
    #如果要求手动安排再考虑display函数
    # def display(self):
    #     #display people's situation
    #     print()

