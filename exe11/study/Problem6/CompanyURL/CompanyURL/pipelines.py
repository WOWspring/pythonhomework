# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CompanyurlPipeline:
    def process_item(self, item, spider):
        return item


class tempinfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('BaiduStockInfo.txt', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
            # print("这里用来检查item传递的数据是什么，怀疑是这边的dict结构有问题")
            # print(item)
        except:
            pass
        return item