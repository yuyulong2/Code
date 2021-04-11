# -*-coding:utf-8-*-

'''
@File  :seek_fun.py
@Author:yuyulong
@Date  :2021/4/10 17:48
@Desc  :
'''
# https://chs.meituan.com/meishi/
# https://chs.meituan.com/meishi/pn2/
# https://chs.meituan.com/meishi/pn3/

# 时间转换
import time

# 获得当前时间时间戳
now = int(time.time())
print(now)
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

timeStamp = 1618052123901
timeStamp = int(timeStamp)
print(timeStamp)
timeArray = time.localtime(int(timeStamp))
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

