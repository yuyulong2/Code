# -*-coding:utf-8-*-

'''
@File  :meituan1.py
@Author:yuyulong
@Date  :2021/4/10 15:57
@Desc  :
'''

import requests
import re

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_lxsdk_cuid=178b6fd8dbcc8-037932c85c7754-c3f3568-144000-178b6fd8dbcc8; ci=70; rvct=70; client-id=1efd798f-9460-4e1e-8f6f-fab5d6221c72; mtcdn=K; lsu=; _hc.v=4a388759-acb6-cb76-fb85-49314f5180f2.1618042117; uuid=546cc19e90f3476d818a.1618052108.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=188586263.1617977786679.1618047689309.1618052108900.5; u=760080353; n=%E9%99%8C%E5%A2%A8%E4%BA%91%E4%B9%A6; lt=2oSZeAiuEqSKPr1k20g-csMdEoQAAAAAKg0AAEocaehemZ-Pe62yMjOiN-IrGVxy5G-aMUrRjepVGA34KWzzYookKwh7iWXtfeKZpw; mt_c_token=2oSZeAiuEqSKPr1k20g-csMdEoQAAAAAKg0AAEocaehemZ-Pe62yMjOiN-IrGVxy5G-aMUrRjepVGA34KWzzYookKwh7iWXtfeKZpw; token=2oSZeAiuEqSKPr1k20g-csMdEoQAAAAAKg0AAEocaehemZ-Pe62yMjOiN-IrGVxy5G-aMUrRjepVGA34KWzzYookKwh7iWXtfeKZpw; token2=2oSZeAiuEqSKPr1k20g-csMdEoQAAAAAKg0AAEocaehemZ-Pe62yMjOiN-IrGVxy5G-aMUrRjepVGA34KWzzYookKwh7iWXtfeKZpw; firstTime=1618052123901; unc=%E9%99%8C%E5%A2%A8%E4%BA%91%E4%B9%A6; _lxsdk_s=178bb8a6585-819-073-624%7C%7C1',
    'Host': 'chs.meituan.com',
    'Referer': 'https://chs.meituan.com/meishi/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
url = 'https://chs.meituan.com/meishi/'
res = requests.get(url,headers=headers)
print(res.status_code)
fout = open("meituan1.html", 'w', encoding='utf-8')
fout.write(res.text)
fout.close()
