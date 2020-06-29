# -*- coding: utf-8 -*-
import scrapy
import re


class SearchcompanyinfoSpider(scrapy.Spider):
    name = 'SearchCompanyInfo'
    allowed_domains = ['tianyancha.com']
    start_urls = ['http://tianyancha.com/']

    def getCompanyName(self, fpath = 'D:\gitwork\pythonhomework\exe11\Problem6\CompanyURL\CompanyName.txt'):
        '''
        遍历fpath读取公司名称形成一个列表
        :param fpath:
        :return:
        '''
        company_name_list = []
        with open('CompanyName.txt', 'r', encoding='utf-8') as f:
            temp = f.readline()
            while len(temp) != 0:
                company_name_list.append(temp)
                print(temp)
                temp = f.readline()
        return company_name_list

    def start_requests(self):
        '''
        利用公司名字生成搜索的url，生成器callback解析搜索网页的函数
        exp: https://www.tianyancha.com/search?key=
        :return:
        '''
        company_name_list = self.getCompanyName()
        urls = [['https://www.tianyancha.com/search?key=' + name, name] for name in company_name_list]
        for url in urls:
            #断点print检查
            print(url)
            #meta传递公司名称，方便parse_search解析response
            yield scrapy.Request(url=url[0], callback=self.parse_search, meta=url[1])
        #测试用
        # url = ['https://www.tianyancha.com/search?key=中国华戎科技集团有限公司', '中国华戎科技集团有限公司']
        # yield scrapy.Request(url=url[0], callback=self.parse_search, meta={'name': url[1]})

    def parse(self, response):
        pass

    def parse_search(self, response):
        '''
        根据spider发回的search利用css查找出该公司在天眼查中的信息网页，然后callback解析公司信息的函数
        :param response:
        :return:
        '''
        company_name = response.meta['name']
        company_search_url = response.css('name select-none::attr(href)').extract()[0]    #得到匹配程度最高的目标
        # print('============此处检查response的文本==========')
        # # pat = re.compile(r'class=\"name select-none \".*target=\'_blank\'')
        # # result = pat.findall(response.text)
        # print(len(response.text))
        # print(type(response.text))
        # print('==================检查结束==================')
        company_Dict = {
            '公司名称': company_name,
            # '目标网页代码': response.text,
            '公司主页': company_search_url
                        }
        yield company_Dict