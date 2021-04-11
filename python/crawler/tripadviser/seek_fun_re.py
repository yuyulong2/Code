# -*-coding:utf-8-*-

'''
@File  :seek_fun_re.py
@Author:yuyulong
@Date  :2021/4/1010:46
@Desc  :
'''
import re

a = '"detailPageUrl": "/Restaurant_Review-g60763-d12425739-Reviews-Piccola_Cucina_Estiatorio-New_York_City_New_York.html",'
f_restaurant = open('tripadviser1.html', 'r', encoding='utf-8')
restaurants_detailPageUrl = re.findall('"detailPageUrl": "(.*)",', f_restaurant.read())
# print(restaurants_detailPageUrl)

# restaurants_all = re.findall('"restaurants": (.*)}, "error": null',f_restaurant.read())
# print(restaurants_all) 太长了无法查取
for i in range(0, 120, 30):
    print(i)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = []
c.append(a)
print(c)
a.extend(b)
print(a)

import pandas as pd

# a = pd.DataFrame(a)
# a.to_csv('a.csv')
#
# restaurant_list = []
# fout = open('tripadviser2.html','r+', encoding='utf-8')
# # restaurants_detailPageUrl = re.findall('"detailPageUrl": "(.*)",', res.text)
# restaurants_detailPageUrl = re.findall('"detailPageUrl": "/Restaurant_Review-g60763-(.*?)-New_York_City_New_York.html"', fout.read())
# restaurant_list.extend(restaurants_detailPageUrl)
# fout.close()
# restaurant_url = pd.DataFrame(restaurant_list)
# restaurant_url.to_csv('restaurant60.csv')

restaurant_data = pd.read_csv('restaurant60.csv')
# print(restaurant_data.iloc[:, 1])
restaurant_data = restaurant_data.iloc[:, 1].drop_duplicates()
restaurant_data.to_csv('restaurant60_drop_duplicates.csv')
