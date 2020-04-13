# -*- encoding: utf-8 -*-
'''
@File : 03_dictfunc.py
@Time : 2020/04/12 22:17:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass:
    mydict = {}

    def __init__(self, mydict):
        self.mydict = mydict
    
    def del_dict(self, dkey):
        del self.mydict[dkey]

    def get_dict(self, dkey):
        if dkey in self.mydict:
            return self.mydict[dkey]
        else:
            return 'not found'
    
    def get_key(self):
        return [k for k, v in self.mydict.items()]

    def update_dict(self, anodict):
        for k, v in anodict.items():
            self.mydict[k] = v
        return [v for k, v in self.mydict.items()]
    

rawdict = {
    'a': 1,
    'b': 3,
    'c': 7
    }

rawdict2 = {
    'd': 2,
    'e': 9,
    'f': 10
}

newdict = dictclass(rawdict)
newdict.del_dict('b')
print(newdict.mydict)
print(newdict.get_dict('b'))
print(newdict.get_dict('c'))
print(newdict.get_key())
print(newdict.update_dict(rawdict2))
# print('c' in rawdict)