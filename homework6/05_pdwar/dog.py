# -*- encoding: utf-8 -*-
'''
@File : dog.py
@Time : 2020/04/13 16:47:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class dogc:
    '''
    狗类，初始化方法会新置血量，攻击力
    被咬后会降低血量和攻击力，并且刷新生命状态和攻击状态
    '''
    def __init__(self):
        self.attack = 15
        self.life = 80
        self.status = True  #True means alive, False means dead
        #self.fesibattc = True   #True means still can fight, False means cannot combat
    
    def dbitetd(self, damage):
        #Being bitetd will decrease 3 attack and resume life equals to damage
        if damage != 0:
            if self.attack != 0:
                self.attack -= 3
        self.life -= damage
        if self.life <= 0:
            self.status = False
        if self.attack <= 0:
            self.fesibattc = False
