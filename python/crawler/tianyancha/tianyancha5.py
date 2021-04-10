import requests
from bs4 import BeautifulSoup
url = 'http://www.tianyancha.com/company/2310290454'
header = {
    'Host': 'www.tianyancha.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Tyc-From': 'normal',
    'CheckError': 'check',
    'Connection': 'keep-alive',
    'Referer': 'http://www.tianyancha.com/company/2310290454',
    'Cache-Control': 'max-age=0',
    'Cookie': 'jsid=SEM-BAIDU-PZ-SY-2021112-JRGW; TYCID=cf0b6d808e0711ebb201db629f04d64b; ssuid=5997346390; '
              'sajssdk_2015_cross_new_user=1; _ga=GA1.2.227538246.1616744982; _gid=GA1.2.1931441579.1616744982; '
              'searchSessionId=1616745002.89113430; RTYCID=978710bd7df24a9497e6c059873d7001; '
              'CT_TYCID=e67f29f1503b4ef9998858dc3c8c9a4e; tyc-user-info={"claimEditPoint":"0","explainPoint":"0",'
              '"vipToMonth":"false","personalClaimType":"none","integrity":"20%","state":"0","score":"33",'
              '"anonymityLogo":"https://static.tianyancha.com/design/anonymity/anonymity1.png",'
              '"announcementPoint":"0","messageShowRedPoint":"0","vipManager":"0","monitorUnreadCount":"0",'
              '"discussCommendCount":"0","onum":"0","showPost":null,'
              '"messageBubbleCount":"0","claimPoint":"0",'
              '"token":"eyJhbGciOiJIUzUxMiJ9'
              '.eyJzdWIiOiIxNTE2MjEyMzc3MyIsImlhdCI6MTYxNjc0ODAwOCwiZXhwIjoxNjQ4Mjg0MDA4fQ.ca3pijNqtKBpk4'
              '-Qqdqc6SXtbzCFrvYotJsPbBTFZTKxrFLt4Qgp2UJcDB9WJmfD9xbJOvjKLXuPIgaZRR7UDQ","schoolAuthStatus":"2",'
              '"userId":"39771922","scoreUnit":"","redPoint":"0","myTidings":"0","companyAuthStatus":"2",'
              '"originalScore":"33","myAnswerCount":"0","myQuestionCount":"0","signUp":"0",'
              '"privateMessagePointWeb":"0",'
              '"headPicUrl":"https://cdn.tianyancha.com/design/avatar/pastDefaultHeadUrl.png",'
              '"privateMessagePoint":"0","bossStatus":"2","isClaim":"0","yellowDiamondEndTime":"0",'
              '"yellowDiamondStatus":"-1","pleaseAnswerCount":"0","bizCardUnread":"0","vnum":"0",'
              '"mobile":"15162123773","riskManagement":{"servicePhone":null,"mobile":15162123773,"title":null,'
              '"currentStatus":null,"lastStatus":null,"quickReturn":false,"oldVersionMessage":null,'
              '"riskMessage":null}}; tyc-user-info-save-time=1616748006272; '
              'auth_token=eyJhbGciOiJIUzUxMiJ9'
              '.eyJzdWIiOiIxNTE2MjEyMzc3MyIsImlhdCI6MTYxNjc0ODAwOCwiZXhwIjoxNjQ4Mjg0MDA4fQ.ca3pijNqtKBpk4'
              '-Qqdqc6SXtbzCFrvYotJsPbBTFZTKxrFLt4Qgp2UJcDB9WJmfD9xbJOvjKLXuPIgaZRR7UDQ; '
              'tyc-user-phone=%5B%2215162123773%22%5D; bannerFlag=true; '
              'Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1616744982,1616758546; sensorsdata2015jssdkcross={'
              '"distinct_id":"39771922","first_id":"1786d8295da18e-0919033465e07a-5771031-1327104-1786d8295db77b",'
              '"$latest_referrer":""},"$device_id":"1786d8295da18e-0919033465e07a-5771031-1327104-1786d8295db77b"}; '
              'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1616758996; cloud_token=2f17a82421514d9c90c3bc0fccde225c '
}
r = requests.get(url, headers=header)
print(r.status_code)
# fout = open('tianyancha5.html', 'w', encoding='utf-8')
# fout.write(r.text)
# fout.close()
soup = BeautifulSoup(r.text, 'lxml')

