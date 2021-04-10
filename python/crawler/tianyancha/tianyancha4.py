# -*- coding: utf-8 -*-
import re
import csv
import scrapy
import redis
redis_cli = redis.Redis(host='127.0.0.1',port=6379)


class SearchSpider(scrapy.Spider):
    name = 'search'
    # num = 0
    allowed_domains = ['www.tianyancha.com']
    start_urls = ['http://www.tianyancha.com/']
    dr = re.compile(r'<[^>]+>', re.S)
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host':'www.tianyancha.com',
        'Referer':'www.tianyancha.com',
    }
    cookies='aliyungf_tc=AQAAAP6muX9DyAsAtlH3Oqxg8RT+o/Ue; csrfToken=JgvbpACNlq9x03jd8-YRyQpo; TYCID=4eed97a0de4a11e8a64ebdb872e198de; undefined=4eed97a0de4a11e8a64ebdb872e198de; ssuid=425167980; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1541127139; _ga=GA1.2.1870685403.1541127140; _gid=GA1.2.857435514.1541127140; token=8463eed85217427b92358c2828d546b2; _utm=4fe67a08ebed4970858bf216a50c247d; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252258%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzYyMTk4OTkyMyIsImlhdCI6MTU0MTEyNzE2NSwiZXhwIjoxNTU2Njc5MTY1fQ.uBNhmJ563KfA6tyJAk-pc54yGYThirDuKDBPStBzHHvAEYJ3gQ4lnDLxugKJzQ0enXXs59uESKjTPXtRQ65LrQ%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217621989923%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzYyMTk4OTkyMyIsImlhdCI6MTU0MTEyNzE2NSwiZXhwIjoxNTU2Njc5MTY1fQ.uBNhmJ563KfA6tyJAk-pc54yGYThirDuKDBPStBzHHvAEYJ3gQ4lnDLxugKJzQ0enXXs59uESKjTPXtRQ65LrQ; RTYCID=6fd9880e3de246acbff6beaedbc9ec77; CT_TYCID=f41090929ec847f8b63b73608a8cbd0b; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1541131237; _gat_gtag_UA_123487620_1=1; cloud_token=3d67526240bf4f3c9aaff7f004d8e522; cloud_utm=1bd3d1e102e441d39f7560aaef75b87e'

    cookie={}
    # f = open('C:tianyancha_car.txt', 'w', encoding='utf-8')
    for c in cookies.split(';'):
        cookie[c.split('=')[0]]=c.split('=')[1]
    def start_requests(self):
        # for id in idlist:

        with open('/Users/admin/Downloads/tianyancha/tianyancha/needs.csv')as g:
            reader = csv.reader(g)
            num = 0
            for row in reader:
                num+=1
                id = row[3]
                # 爬过的去重
                reuslt = redis_cli.sismember('tianyancha', id)
                # print(reuslt)
                if not reuslt:
                    print(row)
                    meta={'oldinfo':row,'num':num}
                    yield scrapy.Request(url='https://www.tianyancha.com/search?key=%s'%id,
                                         callback=self.index_parse,headers=self.headers,cookies=self.cookie,
                                         meta=meta)
    def index_parse(self, response):
        try:
            url = response.xpath('//a[@class="name "]/@href').extract()[0]
            # for element in response.css('#web-content > div > div.container-left > div > div.result-list>div'):
            #     url=element.css('div.header>a.name::attr(href)').extract()[0]
            yield scrapy.Request(url=url,
                                 callback=self.parse_campany,headers=self.headers,cookies=self.cookie,
                                 meta=response.meta)
        except:
            oldinfo = response.meta['oldinfo']
            print('提取详情页失败{}'.format(oldinfo))
            redis_cli.sadd('tianyancha',oldinfo[3])

            with open('searchfailed.csv','a',encoding='utf-8',newline='')as j:
                writer = csv.writer(j)
                writer.writerow(oldinfo)
                print('存入失败csv')


    def parse_campany(self, response):
        # print(response.text)
        oldinfo = response.meta['oldinfo']

        # try:
        # 企业名称
        # campany=response.css('#company_web_top > div.box > div.content > div.header > h1.name::text').extract()[0]
        # zzjgdm=response.meta['id']
        # 行业
        try:
            hy=response.css('#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(3) > td:nth-child(4)::text').extract()[0]
        except:
            hy=''
        # 登记机关
        try:
            djjj=response.css('#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(6) > td:nth-child(4)::text').extract()[0]
        except:
            djjj=''
        # 地址
        try:
            zcdz=response.css('#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(8) > td:nth-child(2)::text').extract()[0]
        except:
            zcdz=''
        # 经营范围
        try:
            jyfw = response.xpath('//span[@class="js-full-container"]/text()').extract()[0]
            if not jyfw:
                jyfw=self.dr.sub('',response.css('#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(9) > td:nth-child(2)').extract()[0])
            # if '详情' in jyfw:
        except:
            jyfw=''
        # 简介
        try:
            introduction=response.xpath('//div[@class="summary"]/span[2]/text()').extract()[0]
            if introduction != '暂无信息':
                introduction=response.xpath('//div[@class="summary"]/script[1]/text()').extract()[0].strip()

        except:
            introduction=''
        #状态
        try:
            status = response.xpath('//div[contains(./text(),"公司状态")]/following::div[1]/@title').extract()[0]
        except:
            status=''
        # 电话
        # phone = response.xpath('//div[@class="detail"]/div[1]/div[1]/span[2]/text()').extract()[0]
        try:
            phone = response.xpath('//span[contains(./text(),"电话：")]/following::span[1]/text()').extract()[0]
        except:
            phone=''
        # 网址
        # site = response.xpath('//div[@class="detail"]/div[2]/div[1]/span[2]/text()').extract()[0]
        try:
            site = response.xpath('//span[contains(./text(),"网址")]/following::span[1]/text()').extract()[0]
        except:
            site=''
        # 注册资本
        try:
            register_money = response.xpath('//tbody/tr[1]/td[2]/div[2]/@title').extract()[0]
        except:
            register_money=''
        # 注册时间
        # register_time = response.xpath('')
        try:
            register_time = '加密'
        except:
            register_time = ''
        # 公司类型
        try:
            company_type = response.xpath('//td[contains(./text(),"公司类型")]/following::td[1]/text()').extract()[0]
        except:
            company_type = ''
        #组织机构代码
        try:
            company_code = response.xpath('//td[contains(./text(),"组织机构代码")]/following::td[1]/text()').extract()[0]
        except:
            company_code = ''
        for i in [hy,djjj,zcdz,jyfw,introduction,status,phone,site,register_money,register_time,company_type,company_code]:
            oldinfo.append(i)
        with open('result2.csv','a',encoding='utf-8',newline='')as h:
            writer = csv.writer(h)
            writer.writerow(oldinfo)
            num = response.meta['num']
            print('第{}个写入完成  ---- {}'.format(num,oldinfo[3]))
            redis_cli.sadd('tianyancha',oldinfo[3])
        # except Exception as e :
        #     print('数据解析失败',e)
        #     with open('failed.csv','a',encoding='utf-8',newline='')as j:
        #         writer = csv.writer(j)
        #         writer.writerow(oldinfo)
        #         print('存入失败csv')


# import csv
# all=[]
# with open('/Users/admin/Downloads/tianyancha/tianyancha/needs.csv')as g:
#     reader = csv.reader(g)
#
#     for row in reader:
#         all.append(row[3])
# print(len(all))
# print(len(set(all)))

