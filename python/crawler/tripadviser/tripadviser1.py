# -*-coding:utf-8-*-
#
# https://www.tripadvisor.cn/Restaurants-g60763-New_York_City_New_York.html
import requests

res = requests.get("https://www.tripadvisor.cn/Restaurants-g60763-New_York_City_New_York.html")
print(res.status_code)
fout = open('tripadviser1.html','w',encoding='utf-8')
fout.write(res.text)
fout.close()