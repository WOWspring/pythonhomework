# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import bs4
from parse_data import count_salary
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
    job_count = 0

    def start_requests(self):
        for page in range(1, MAX):
            url = self.base_urls_top + self.search_target + self.base_urls_middle + str(page) + self.base_urls_botton
            # print('当前正在解析读取数据的页面为：' + url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        # url = self.base_urls_top + self.search_target + self.base_urls_middle + str(1) + self.base_urls_botton
        # yield scrapy.Request(url=url, callback=self.parse_page)

    def parse(self, response):
        pass

    def parse_page(self, response):
        job_info_dict = {}

        soup = BeautifulSoup(response.body.decode('gbk'), "html.parser")
        job_skim = soup.find_all('div', class_='dw_table', id="resultList")[0]
        job_skim: bs4.element.Tag
        job_info_list = job_skim.find_all('div', class_='el')[1:]
        for item in job_info_list:
            item: bs4.element.Tag
            tempsalary = 0
            if item.find('span', class_='t4').text != '':
                tempsalary = count_salary(str(item.find('span', class_='t4').text).split()[0])
            job_info_dict[str(self.job_count)] = {
                    '职位名': str(item.find('p', class_='t1').text).split()[0],
                    '公司名': str(item.find('span', class_='t2').text).split()[0],
                    '工作地点': str(item.find('span', class_='t3').text).split()[0],
                    '薪资': tempsalary,
                    '发布时间': str(item.find('span', class_='t5').text).split()[0]
                }
            self.job_count = self.job_count + 1

        yield job_info_dict