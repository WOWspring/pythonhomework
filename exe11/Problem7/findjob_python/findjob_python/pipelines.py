# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FindjobPythonPipeline:
    def process_item(self, item, spider):
        return item


class JobInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('JobInfo.txt', 'w')
        self.f.write('职位名 公司名 工作地点 薪资 发布时间')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider, key_list=None):
        try:
            item: dict
            key_list = list(item.keys())
            key_list.sort()
            for key in key_list:
                bufstring = '{} {} {} {} {}\n'.format(item[key]['职位名'], item[key]['公司名'], item[key]['工作地点'], item[key]['薪资'], item[key]['发布时间'])
                self.f.write(bufstring)
        except:
            pass
        return item