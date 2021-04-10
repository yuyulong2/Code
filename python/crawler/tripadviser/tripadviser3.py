# -*-coding:utf-8-*-

'''
@File  :tripadviser3.py
@Author:yuyulong
@Date  :2021/4/10 14:03
@Desc  :
'''
#爬取tripadvisor纽约市酒店超值排名

#引入requests 获取html文件，才能从html获取信息
import requests
#利用BeautifulSoup解析文件，获取想要的到的数据
from bs4 import BeautifulSoup
#这段代码只用在获取等待，避免频繁访问ip被封禁
import time

#url = 'https://www.tripadvisor.cn/Hotels-g60763-oa30-New_York_City_New_York-Hotels.html'
#获取全部的url。每一页的url不同
urls = ['https://www.tripadvisor.cn/Hotels-g60763-oa{}-New_York_City_New_York-Hotels.html'.format(str(i)) for i in range(0,720,30)]
#利用headers假装是浏览器，可以在网页检查，NetWork里面找
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

#定义函数找到所需要的信息
def get_hotel(url):
    #每次调用等待两秒
    time.sleep(2)
    #利用requests请求的到html
    resp = requests.get(url)
    #利用BeautifulSoup解析，利用率lxml解析库
    soup = BeautifulSoup(resp.text,'lxml')

    #css选选择器选择所需要的信息，包括标题，价格，和排名
    #imgs = soup.select('div.aspect.is-hidden-tablet > div.inner')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    paimings = soup.select('div.popindex')
    prices = soup.select('div.xwrap')

    #存储在一个字典里面
    for title,paiming,price in zip(titles,paimings,prices):
        data = {
            'title':title.get_text(),
            'paiming':paiming.get_text(),
            'price':price.get_text(),
        }
        print(data)

#对每一个页面都爬取，
for url in urls:
    get_hotel(url)
