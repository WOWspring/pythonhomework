# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from settings import MAX_PAGECRAWL_NUMBER as MAX
from urllib.parse import quote

class FindjobSpider(scrapy.Spider):
    name = 'findjob'
    allowed_domains = ['51job.com']
    #该网址为python+全国的检索结果
    base_urls_top = 'https://search.51job.com/list/000000,000000,0000,00,9,99,'
    base_urls_middle = ',2,'
    base_urls_botton = '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    search_target = 'Python'
    # start_urls = [base_urls_top + search_target + base_urls_botton]

    def start_requests(self):
        # for page in range(1, MAX):
        #     url = self.base_urls_top + self.search_target + self.base_urls_middle + str(page) + self.base_urls_botton
        #     # print('当前正在解析读取数据的页面为：' + url)
        #     yield scrapy.Request(url=url, callback=self.parse_page)
        url = self.base_urls_top + self.search_target + self.base_urls_middle + str(1) + self.base_urls_botton
        yield scrapy.Request(url=url, callback=self.parse_page)

    def parse(self, response):
        pass

    def parse_page(self, response):
        job_info_dict = {}

        soup = BeautifulSoup(response.body.decode('gbk'), "html.parser")
        # position = response.css('.el').extract()
        # job_title_list = position.css('.t1 tg1::text').extract()
        # company_name_list = position.css('.t2:text').extract()
        # working_location_list = position.css('.t3:text').extract()
        # salary_list = position.css('.t4:text').extract()    #处理
        # publish_datetime_list = position.css('.t5:text').extract()

        for i in range(len(job_title_list)):
            job_info_dict.update(
                {
                    '职位名': job_title_list[i],
                    '公司名': company_name_list[i],
                    '工作地点': working_location_list[i],
                    '薪资': salary_list[i],
                    '发布时间': publish_datetime_list[i]
                })
        yield job_info_dict
        #测试用
        # print('==============================================')
        # print(response.body.decode('gbk'))
        # print('==============================================')
        # yield {'网页原文': response.body.decode('gbk')}