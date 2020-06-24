# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sql.jobsql import SQL
from sql.jobsql import chart_clear


class FindjobPythonPipeline:
    def process_item(self, item, spider):
        return item


class JobInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('data/jobinfo.txt', 'w')
        self.f.write('职位名 公司名 工作地点 薪资 发布时间')
        self.pw = input('Please input a password: ')
        self.sql = SQL(self.pw)
        chart_clear(self.sql)
        # self.sql.alter_id()

    def close_spider(self, spider):
        self.f.close()
        self.sql.exit()

    def process_item(self, item, spider, key_list=None):
        try:
            item: dict
            key_list = list(item.keys())
            key_list.sort()
            for key in key_list:
                buff_string = '{} {} {} {} {}\n'.format(item[key]['职位名'], item[key]['公司名'], item[key]['工作地点'], item[key]['薪资'], item[key]['发布时间'])
                self.f.write(buff_string)
                self.sql.insert(item[key]['职位名'], item[key]['公司名'], item[key]['工作地点'], item[key]['薪资'], item[key]['发布时间'])
        except:
            pass
        return item