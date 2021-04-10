# -*-coding:utf-8-*-

'''
@File  :tripadviser4.py
@Author:yuyulong
@Date  :2021/4/10 15:35
@Desc  :
'''
import pandas as pd
data = pd.read_csv('restaurant1800.csv')

# https://www.tripadvisor.cn/Restaurant_Review-g60763-d4363835-Reviews-Piccola_Cucina_Osteria-New_York_City_New_York.html

if __name__ == '__main__':
    for i in range(2):
        print(data.iloc[i,0])
        print('https://www.tripadvisor.cn/Restaurant_Review-g60763-{}-New_York_City_New_York.html'.format(data.iloc[i,0]))
