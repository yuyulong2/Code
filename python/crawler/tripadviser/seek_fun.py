# -*-coding:utf-8-*-

import requests

# https://www.tripadvisor.cn/Restaurants-g60763-New_York_City_New_York.html
# https://www.tripadvisor.cn/Restaurants-g60763-New_York_City_New_York.html
# https://www.tripadvisor.cn/Restaurants-g60763-New_York_City_New_York.html

# 使用ajax传递数据
# 第三页61-90
# https://www.tripadvisor.cn/Restaurant_Review-g60763-d543689-Reviews-Tony_s_Di_Napoli_Midtown-New_York_City_New_York.html
# https://www.tripadvisor.cn/Restaurant_Review-g60763-d8069276-Reviews-Nomo_Soho_Restaurant-New_York_City_New_York.html


# 厦门市餐厅搜索
# https://www.tripadvisor.cn/Restaurants-g297407-Xiamen_Fujian.html

# urls = ['https://www.tripadvisor.cn/Restaurants-g297407-Xiamen_Fujian.html']
# res = ''
# for url in urls:
#     res = requests.get(url)
#
# fout = open('tripadviser1.html','w',encoding='utf-8')
# fout.write(res)
# fout.close()
import pandas as pd
# 多个表格合并
restaurant300 = pd.read_csv('restaurant300_drop_duplicates.csv')
restaurant600 = pd.read_csv('restaurant600_drop_duplicates.csv')
restaurant1800 = pd.read_csv('restaurant1800_drop_duplicates.csv')
import pandas as pd
import glob
import os


all_files = glob.glob(os.path.join("*drop_duplicates.csv"))    # 遍历当前目录下的所有以.csv结尾的文件
all_data_frame = []
row_count = 0
for file in all_files:
    data_frame = pd.read_csv(file)
    all_data_frame.append(data_frame)
    # axis=0纵向合并 axis=1横向合并
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True, sort=True)
data_frame_concat.to_csv("restaurant1800.csv", index=False, encoding="utf-8")     # 将重组后的数据集重新写入一个文件

