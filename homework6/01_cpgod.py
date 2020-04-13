# -*- encoding: utf-8 -*-
'''
@File : 01_cpgod.py
@Time : 2020/04/12 18:19:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#        实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class cpdog:
    '''
    这个类用于保存不同品种的狗的库存情况
    '''

    store_dog = [
        {
            'color': 'yellow',
            'number': 18,
            'price': 200
        },
        {
            'color': 'red',
            'number': 25,
            'price': 150
        },
        {
            'color': 'green',
            'number': 200,
            'price': 10
        }
    ]

    def sell_dog(self, sell_number, sell_kind):
        '''
        参数为出售的数量和出售的品种，如果不符合店家的购买要求（数量不够或者没有品种）则输出抱歉语句，
        否则提示出售成功并且返回出售的金额
        '''
        if sell_kind == 'yellow':
            if sell_number > self.store_dog[0]['number']:
                print('We dont have enough dogs you want for sell,Sorry.')
            else:
                print('Successfully sell {} dogs, which kind is {}'.format(sell_number, self.store_dog[0]['color']))
                self.store_dog[0]['number'] -= sell_number
                return self.store_dog[0]['price'] * sell_number
        elif sell_kind == 'red':
            if sell_number > self.store_dog[1]['number']:
                print('We dont have enough dogs you want for sell,Sorry.')
            else:
                print('Successfully sell {} dogs, which kind is {}'.format(sell_number, self.store_dog[1]['color']))
                self.store_dog[1]['number'] -= sell_number
                return self.store_dog[1]['price'] * sell_number
        elif sell_kind == 'green':
            if sell_number > self.store_dog[2]['number']:
                print('We dont have enough dogs you want for sell,Sorry.')
            else:
                print('Successfully sell {} dogs, which kind is {}'.format(sell_number, self.store_dog[2]['color']))
                self.store_dog[2]['number'] -= sell_number
                return self.store_dog[2]['price'] * sell_number
        else:
            print('We dont have dogs you want, Sorry')

    def purchase_dog(self, buy_number, buy_kind):
        '''
        输入参数为购买的数量和购买的品种，不是以上三种的视作购买失败，简化上面的出售语句，显得过于繁琐，可以在最初做条件语句
        返回值为购买所花的金额
        '''
        flag = -1
        if buy_kind == 'yellow':
            flag = 0
        elif buy_kind == 'red':
            flag = 1
        elif buy_kind == 'green':
            flag = 2
        
        if flag == -1:
            print('This dog is not what we want')
        else:
            self.store_dog[flag]['number'] += buy_number
            print('Successfully Purchased! Now we have {} {} dogs!'.format(self.store_dog[flag]['number'], self.store_dog[flag]['color']))
            return buy_number * self.store_dog[flag]['price']

X = cpdog()
X.sell_dog(50, 'yellow')
X.sell_dog(10,'green')
X.purchase_dog(80,'red')
X.purchase_dog(50,'yellow')
X.sell_dog(51, 'yellow')