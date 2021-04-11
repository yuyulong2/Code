# -*-coding:utf-8-*-

'''
@File  :meituan4.py
@Author:yuyulong
@Date  :2021/4/10 20:08
@Desc  :
'''
# Request URL: https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn1%2F&riskLevel=1&optimusCode=10&_token=eJyFT8uSmzAQ%2FBddQxkBQoCrcjAPv9bYBoyNvbUHDDKGxQ%2BQgIVU%2Fj3aZHPIKZfpnu6urpkfoF6kYCxBaEAogJbUYAykERxhIABGuYMlHapYhZqhIwEk%2F2h8KgI413sbjF8lpCFB1vW3T8XnwqukKljQMXoT%2Fpi%2FqcxD6DOz4BFwZexJx6KYXOnoRnLWxPdR8riJnNNrLj7vksgP%2BW9KFgGvvO14Jcf3L4y%2FkP3dXf4cr6N5dueMLLuyCKXK653weiFBFm4MtQlPjmJ6bl45Q%2F2YwBPV%2B4s7b724f5%2F0uDjgrOlLONX2MLXRRpXT4sV4Rmc0UQMx22a%2B2q6rlUoi1bgoqJtLK4vQhwE95s%2F928FC0VHuS21tLo9148TwztIhXIZy6SzY4BF3byn5mSYfxJLN6SyYvgxHLGfraufLRdpV%2B%2FK0KqWhoDP2YMOWJL6SJHlkE7oRoQYtaNtr5xs1iL1ty%2Fm2zyYE7VaNoZfPqseHYNbEzHRhaXb4HOGWBl34Hfz8BXp4neM%3D
# Request URL: https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=2&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn2%2F&riskLevel=1&optimusCode=10&_token=eJyFj0tzokAUhf9Lb6VsGpuXVVmAisVDjEgrmsoCEAR5hoeIU%2FPf08lkFrOa1Tn33K9O3fsLNPoFzBHLyizLgHvUgDlAU3YqAAZ0Ld0ISGJ5gRexjDkGhP9kPIskBgTNYQnmbwiLmOEk6f0rcWjwhviZwEgCfmf%2BLL8tRyH8xegUAUnX1e0cwjBpp0WUdr1fTsOqgNS3SQrrkoP0kP9SCAJaWbi0kmr2o%2F6Pdn%2FnDX2O1rXptaQuMob86aJeGVdE3S7E3lysHgL2MHslmd%2FpxK1iZbN%2BapzHr9wh5fdKHV5RrFuRwWv9ybQP0uOYFOfx7mvcRNmSO76xizh4%2BmnvQRnawqTYSfXJneVln54%2FdLwd8WEhbjny6lSGZV%2BGZZSHtrjZ5%2FEpS7Q2uD3SipOcy60wcUPWxFbyo6h6tm1ae255GMnHo81TgXdS%2B7yMZrLmysOaE%2FisWMv4AuvdTqsKIzrLjiAd48DceuVKR88CEo23Ai8nWWaPo6OGUqEOE6w2G8NSh5cX8PsTXzCdmA%3D%3D
# Request URL: https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=3&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn3%2F&riskLevel=1&optimusCode=10&_token=eJyFkUmTokAQhf9LXSGkFqoovLXixqiIokh39AGFABcQWVx6Yv77FOVMR8xpTvnVy5cZL6N%2BgnISgS6C0IRQBbe4BF2AOrDDgArqSnQY4pAyhjCHRAX7fzRGIFXBrtxYoPuBdENXMeefrbIUwgeihKmc6Z%2FqqykRC5PeeibCAtK6Lqqupu3TqpPFh7oJ887%2BkmmCq%2FSgFTnRRJD%2FurAGxMrMa1dSnYsYWIxRSlRsEElMxUyXZKqYGi0xJJKYkkSXyC4Ts%2FilCR%2BWWwzhQ0wSFgQliSvgS6OCXj6mIpNLMgRRSaYgmYBDQXKWIxVx%2Fk3sm%2FT2iFN7hKjhn1r%2Ffc%2FEzwhrdUhyQbF9P3%2BtkeM%2BB%2Bte3Dej2Zs7vfqLdTobFQfHexSn6WRs7Zbki%2Ff6dL6dJFatDEZkgu3mYR3Z%2BGmdyByX16HRT8Mg0j3tsPCw0ZuGuRbfDM4Xw2zq4Bk9v48vp7BcWKurHyyPyjYZBv0fTxIHOS0yhO0w5%2B79qkS2fodbJ1RsaxyhZ3rdXOxNBJ3y%2FbgKG7Rr5mGzu%2BC6eK5LP8gVU%2B9hwjZ66HsB0woYz4O3Xr1K8DJ5YMc%2F3qh7XuyH%2Fvhyp6NRFZ%2FPSejfXM%2By3b3TIKXOBpUNfv0GA7K%2FNQ%3D%3D
# token更新太快了
# json数据提取和合并

# -*-coding:utf-8-*-
import csv
import json
import sys
import codecs

json_file = 'meituan1.json'

with open(json_file,'r',encoding='utf-8') as json_obj:
    json_data = json.load(json_obj)
# 第一层
print(type(json_data))
print(json_data.keys())
# <class 'dict'>
# dict_keys(['status', 'data'])

# 第二层
print(type(json_data['data']))
print(json_data['data'].keys())
# print(json_data['data'].values())


print(type(json_data['data']['poiInfos']))

for data in json_data['data']['poiInfos']:
    poiId = data['poiId']
    title = data['title']
    avgScore = data['avgScore']
    allCommentNum = data['allCommentNum']
    address = data['address']
    avgPrice = data['avgPrice']
    dealList = data['dealList']
    for deal in dealList:
        deal_title = deal['title']
        price = deal['price']
        soldCounts = deal['soldCounts']








