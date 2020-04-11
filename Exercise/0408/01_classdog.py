# -*- encoding: utf-8 -*-
'''
@File : 01_classdog.py
@Time : 2020/04/08 09:14:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class dog:
    count = 0   #record the number of the dog

    def __init__(self, name, color):
        self.name = name
        self.color = color
        dog.count = dog.count + 1
        # print(f'{self}\'s sound is {self.sound}')
    def bark(self):
        if len(self.name) <= 4:
            return 'wof'
        else:
            return 'awh'
puppy = dog("puppy", 'white')
print('{}\'s sound is {}'.format(puppy.name, puppy.bark()))
wolf = dog('wolf', 'grey')
print('{}\'s sound is {}'.format(wolf.name, wolf.bark()))
tiger = dog('tiger', 'yellow')
print('{}\'s sound is {}'.format(tiger.name, tiger.bark()))

print(f'the number of the dog is {dog.count}')
