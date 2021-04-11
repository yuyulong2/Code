# -*-coding:utf-8-*-

'''
@File  :tripadviser2.py
@Author:yuyulong
@Date  :2021/4/1010:28
@Desc  :
'''
import requests
import re
import pandas as pd
import time
# import pymongo
# client = pymongo.MongoClient('localhost',27017)
# mydb = client['mydb']
# test = mydb['restaurants']
# https://www.tripadvisor.cn/Restaurants-g60763-oa30-New_York_City_New_York.html#EATERY_LIST_CONTENTS
# https://www.tripadvisor.cn/Restaurants-g60763-oa30-New_York_City_New_York.html#EATERY_LIST_CONTENTS
# 查找所有的餐厅url并存入数据库
urls = [
    'https://www.tripadvisor.cn/Restaurants-g60763-oa{}-New_York_City_New_York.html#EATERY_LIST_CONTENTS'.format(str(i))
    for i in range(630, 1801, 30)]
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/67.0.3396.99 Safari/537.36'}

restaurant_list = []
if __name__ == '__main__':
    for url in urls:
        print(url)
        res = requests.get(url)
        # print(res.text)
        print(res.status_code)

        restaurants_detailPageUrl = re.findall('Restaurant_Review-g60763-(.*?)-New_York_City_New_York.html', res.text)

        restaurant_list.extend(restaurants_detailPageUrl)
        # time.sleep(5)
    restaurant_url = pd.DataFrame(restaurant_list)
    restaurant_url.to_csv('restaurant1800.csv')
#   数据去重
    restaurant_data = restaurant_url.iloc[:, 0].drop_duplicates()
    restaurant_data.to_csv('restaurant1800_drop_duplicates.csv')

