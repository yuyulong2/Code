from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
)
driver = webdriver.PhantomJS(executable_path=r'D:\TortoiseGit\bin\phantomjs.exe', desired_capabilities=dcap)

driver.get('http://www.tianyancha.com/company/2310290454')
# 等待5秒，更据动态网页加载耗时自定义
time.sleep(5)
# 获取网页内容
content = driver.page_source.encode('utf-8')
driver.close()
print(content.decode('utf-8'))

fout = open('tianyancha2.html', 'w', encoding='utf-8')
fout.write(content.decode('utf-8'))
fout.close()
