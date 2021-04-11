# -*-coding:utf-8-*-

'''
@File  :meituan2.py
@Author:yuyulong
@Date  :2021/4/10 19:39
@Desc  :
'''
import requests

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
url = 'https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2F&riskLevel=1&optimusCode=10&_token=eJxVjltvqkAUhf%2FLvEJkhtugb7WMPSijcjmgNn1oEQG5qMMIaNP%2Ffqa3h5PsZK299pfs9Q6YswcTBOEYQhl0KQMTgEZwZAIZ8FZcTGRBQ0dIh3gsg%2BT%2FDGEsgzcW2WDyjHSsy5qqvnwmvgiekaGZsmXqL%2FL38cuquphPxhEIyDk%2FtxNFSfJ2VKcFv742o%2BRUK8K3eaGIEkCwdShYoeWPvv4o%2F92paC3Ytsga4dJ5Xx0TxB9uxMs33ZAFFKcu3MaS40l%2BOL8VcOZMc1z6%2B629pdVMmttqmdlmsAuuWe6HVyWESrdbEVd7KnoHD0fFObjHexDDtSV12LLWJHZXweIQUGb1fy3JaZs5ZTtj4S34w8xhm3o5Prfh%2Bh6fFFtfJRcCd1e35AfIH417Q7wL7lQ%2FPxRd3UTRiaNk058r97xs93iV0rRKbhqJmPig77EdT7OGvPlxNqhq3XTII%2BtkWmnpoFJa6hfmDTTuo6dFVgZLNjaOpPkDPv4Bzt6OkA%3D%3D'
res = requests.get(url,headers=headers)
print(res.status_code)
fout = open("meituan2.json", 'w', encoding='utf-8')
fout.write(res.text)
fout.close()

