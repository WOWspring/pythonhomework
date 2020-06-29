# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sql.jobsql import SQL
from sql.jobsql import chart_clear


class FindjobPythonPipeline:
    def process_item(self, item, spider):
        """

        Args:
            item: Dictionary data to be processed.
            spider:The spider layer of the scrapy.

        Returns:
            item.
        """
        return item


class JobInfoPipeline(object):
    def open_spider(self, spider):
        """

        Args:
            spider:The spider layer of the scrapy.

        Returns:
            None
        """
        self.f = open('data/jobinfo.txt', 'w', encoding='gbk')
        self.f.write('职位名 公司名 工作地点 薪资 发布时间')
        print('由于scrapy爬虫爬取速度过快易被当成恶意攻击。请如果没有即刻开始爬取网页请耐心等待。')
        self.pw = input('请输入密码用于连接数据库: ')
        # self.pw = 'password'
        self.sql = SQL(self.pw)
        chart_clear(self.sql)
        # self.sql.alter_id()

    def close_spider(self, spider):
        """

        Args:
            spider: The spider layer of the scrapy.

        Returns:
            None
        """
        self.f.close()
        self.sql.exit()

    def process_item(self, item, spider, key_list=None):
        """

        Args:
            item: Dictionary data to be processed.
            spider: The spider layer of the scrapy.
            key_list: List of key value data used to temporarily store Dictionaries.

        Returns:
            Return item in case other functions need to callback this data.
        """
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