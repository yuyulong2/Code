# -*-coding:utf-8-*-

'''
@File  :meituan3.py
@Author:yuyulong
@Date  :2021/4/10 19:47
@Desc  :
'''
import requests
import time
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
# 'https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page={}&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2F&riskLevel=1&optimusCode=10&_token=eJxVjltvqkAUhf%2FLvEJkhtugb7WMPSijcjmgNn1oEQG5qMMIaNP%2Ffqa3h5PsZK299pfs9Q6YswcTBOEYQhl0KQMTgEZwZAIZ8FZcTGRBQ0dIh3gsg%2BT%2FDGEsgzcW2WDyjHSsy5qqvnwmvgiekaGZsmXqL%2FL38cuquphPxhEIyDk%2FtxNFSfJ2VKcFv742o%2BRUK8K3eaGIEkCwdShYoeWPvv4o%2F92paC3Ytsga4dJ5Xx0TxB9uxMs33ZAFFKcu3MaS40l%2BOL8VcOZMc1z6%2B629pdVMmttqmdlmsAuuWe6HVyWESrdbEVd7KnoHD0fFObjHexDDtSV12LLWJHZXweIQUGb1fy3JaZs5ZTtj4S34w8xhm3o5Prfh%2Bh6fFFtfJRcCd1e35AfIH417Q7wL7lQ%2FPxRd3UTRiaNk058r97xs93iV0rRKbhqJmPig77EdT7OGvPlxNqhq3XTII%2BtkWmnpoFJa6hfmDTTuo6dFVgZLNjaOpPkDPv4Bzt6OkA%3D%3D'
# https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=2&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn2%2F&riskLevel=1&optimusCode=10&_token=eJyFT8uuokAU%2FJfeSoRumpfJXYCK4SGOSCt6MwtAEOR5eYg4mX%2BfvjN3FrOa5CRVp6pSOecHaI0rWECOUziOAY%2B4BQsA59xcBAzoO%2BqIUOYEiceQExADon81iHgGhO1xBRbvEEuY4SH%2B%2Fqm4VHiHAi8yskiVP%2BZvijCdz4xBIyDt%2B6ZbsGyUdvMyzvohqOZRXbKUd2nGNhVi6SH%2FTfEsoJWlRysp5l8YfGH%2Fd9%2FS52hdl90qymJzLF4eHNRpTbTdUhqs5fopYh9zN5IHvUG8OlG3m5eOfGHtjZlwUJvoBhPDjk1BH86Wc5Sfp7S8TI9ARzN1Rx74zi2T8BVkg88qrCPOyr3cnD2%2BqIbs8mHg3YSPS2mHyDe3Nm3nOq7iInKk7aFIznmqd%2BH9mdVIdq%2F30sIt2RBHLU6S5juOZR%2FQ6jiRj2dXZKLgZs5lFfOK7injBolCXm4UfGWb%2FV6vSzO%2BKK4on5LQ2vnV2oCvkiW6YId%2BQfLcmSZXi%2BRSG2dYa7emrY1vb%2BDnLyConXY%3D
urls = ['https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page={}&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn{}%2F&riskLevel=1&optimusCode=10&_token=eJyFT9tuqlAU%2FJf9ChH2hYu%2BFVGBqoCiSJs%2BbIEAyv2i0qb%2FfnZP24fzdJKVzKyZyWStD9CaEZhBUZyKIg9ucQtmAE7EiQx40HfMkaEqSgqeqhJhgfBfTYaYB%2Bf2qIPZKyQK4TEkb1%2FKjgmvUMIyr8pM%2BTb%2FUkTYfGVMFgFp39fdTBDCtJsUcdYPtJyEVSEw3qWZUJdYYIf8N4UEwCoLj1UyvP4g%2FcH%2Bd9%2Bw51hdlyUlY7F1z98P0HbHxUGL59No8%2BSuG985pJtVndneo76uTUM%2F7%2FC7qs2l7clM9J5brLCJrOGhX2Rj1K94i9pmqcxTGkTEEzLHQ4q2pqUQ3xRVdZbF2kYbKX8xqittHX3f%2BMHuwp2SZTB%2FHnEclFJdQGTRUnXvDRdZ5C6ebMpZuhHBMW2OlXWMRLt9uezpAM%2FDlg7nCvX1eGj9oOSmRENYPhLqe4Es1GK8DZ60fp%2BgXfJAtn%2B5SW7uhEvfqO7SatXFeZ5Q%2F%2BZ6uuWG9gC5vlh0Fvj8A14rnGs%3D'.format(i,i) for i in range(2,5)]
for i in range(1,4):
    url = 'https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page={}&userId=760080353&uuid=546cc19e90f3476d818a.1618052108.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn{}%2F&riskLevel=1&optimusCode=10&_token=eJyFT01vm0AU%2FC97BRmWhWWx1IPNhhgCBttQG6Ie1oAMIXzjr0T971236aGnSk%2BaeTOj0XufYLAzMIeybMiyCC75AOYAzuQZBiKYRu5gSGSNEIKJikSQ%2FqsZsi6C4%2FCdgvkrVHVVhFj98VC2XHiFGsIieSh%2FzN9UUfk8MjaPgGKaunEuSWkxzuq8nM6smaVtLXE%2BFqXUNViT%2BCX%2Fj2EJ8NI65KUcqy9kXzj93T3%2BHu8by1PDWe5c3z8i6G%2FuT9EyN43MW2zcRrGiwnvuSj%2B8dZVrr%2Bhxiz7I0tTWB%2FtEJ%2BHpGdmKc77RN7y60wqtlaG3dLNgcaaGUhmEir50WSPlF52QwKpdX%2FG092TVVmwI6K7fx9s34XCyYvPljvK40boaKg5ryObaC5mjXuWDzwSHrjJ4L3pY9Vdca%2B2UDAkzteM5y8dji8%2FdLhr28cUwYgehl0Rn%2BzDBQYFyY7NYFgyO1CpHvz9dkrQJPAv62xv01rbqDpHcBvGOOmnq%2BzdhEYbFDlXfwM9f1imdpQ%3D%3D'.format(i,i)

    try:
        res = requests.get(url,headers=headers)
        print(res.status_code)
    except:
        print('请求失败', res.status_code)

    fout = open("meituan{}.json".format(i), 'w', encoding='utf-8')
    fout.write(res.text)
    fout.close()
    time.sleep(10)