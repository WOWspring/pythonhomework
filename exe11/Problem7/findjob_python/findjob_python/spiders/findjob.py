# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import bs4
from parse.parse_data import count_salary
from settings import MAX_PAGECRAWL_NUMBER as MAX
from url.spider_url import base_urls_middle, base_urls_top, base_urls_bottom


class FindjobSpider(scrapy.Spider):
    name = 'findjob'
    allowed_domains = ['51job.com']
    search_target = 'Python'
    job_count = 0

    def start_requests(self):
        """

        Returns:
            Return a request generator, which callback a class method to parse the response.
        """
        for page in range(1, MAX):
            url = base_urls_top + self.search_target + base_urls_middle + str(page) + base_urls_bottom
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse(self, response):
        pass

    def parse_page(self, response):
        """

        Args:
            response:Accept the data sent back by request.

        Returns:
            Returns a generator, which is the dictionary of job information by parsing the web page.
        """
        job_info_dict = {}

        soup = BeautifulSoup(response.body.decode('gbk'), "html.parser")
        job_skim = soup.find_all('div', class_='dw_table', id="resultList")[0]
        job_skim: bs4.element.Tag
        job_info_list = job_skim.find_all('div', class_='el')[1:]
        for item in job_info_list:
            item: bs4.element.Tag
            temp_salary = 0
            if item.find('span', class_='t4').text != '':
                temp_salary = count_salary(str(item.find('span', class_='t4').text).split()[0])
            job_info_dict[str(self.job_count)] = {
                '职位名': str(item.find('p', class_='t1').text).split()[0],
                '公司名': str(item.find('span', class_='t2').text).split()[0],
                '工作地点': str(item.find('span', class_='t3').text).split()[0],
                '薪资': temp_salary,
                '发布时间': str(item.find('span', class_='t5').text).split()[0]
            }
            self.job_count = self.job_count + 1

        yield job_info_dict
