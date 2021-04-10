import re
from selenium import webdriver
import time
import uuid
import mysqlDao


class mainAll(object):

    def __init__(self):
        self.url = 'https://www.tianyancha.com/login'
        self.username = ''  # 自己的天眼查账号
        self.password = ''  # 自己的密码
        self.word = '淘宝'
        self.driver = self.login()
        # self.getData(self.driver)
        # self.scrapy(self.driver)
        print("ok,the work is done!")

    def login(self):

        # driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(self.url)

        # 模拟登陆
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"). \
            send_keys(self.username)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"). \
            send_keys(self.password)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
        time.sleep(3)
        driver.refresh()
        # driver.get('https://www.tianyancha.com/company/28723141')

        # # 模拟登陆完成，输入搜索内容
        driver.find_element_by_xpath(".//*[@id='home-main-search']").send_keys(self.word)  # 输入搜索内容
        driver.find_element_by_xpath(".//*[@class='input-group-addon search_button']").click()  # 点击搜索
        driver.implicitly_wait(10)
        #
        #
        #
        # # 选择相关度最高的搜索结果 第一条搜索框，然后再
        # tag = driver.find_elements_by_xpath("//div[@class='search_right_item ml10']")
        # btn = tag[0].find_element_by_tag_name('a')
        # print(btn);
        # closeBtn = driver.find_element_by_id("bannerClose")
        # if not closeBtn is None:
        #     closeBtn.click()
        # btn.click()
        # driver.implicitly_wait(5)
        #
        # # 转化句柄
        # now_handle = driver.current_window_handle
        # all_handles = driver.window_handles
        # for handle in all_handles:
        #     if handle != now_handle:
        #         # 输出待选择的窗口句柄
        #         print(handle)
        #         driver.switch_to.window(handle)

        cons = conn_mysql.selectUnFinishCompany()
        for row in cons:
            driver.implicitly_wait(3)
            id = row[0]
            conpanyname = row[1]
            time.sleep(1)
            print("正在查询第" + str(id) + "个【" + conpanyname + "】")
            try:
                self.refsh(driver, id, conpanyname);
            except:
                print("出现异常！！！第" + str(id) + "个【" + conpanyname + "】")
                conn_mysql.updateConpanyFlase(id);
                driver.refresh();
            print("已经完成第" + str(id) + "个【" + conpanyname + "】")
        return driver

    def refsh(self, driver, id, conpanyname):
        # 模拟登陆完成，输入搜索内容
        driver.find_element_by_xpath("//input[@class='search_input form-control "
                                     "search_form input search-input-v1 f12 "
                                     "js-live-search']").clear();
        driver.find_element_by_xpath("//input[@class='search_input form-control "
                                     "search_form input search-input-v1 f12 "
                                     "js-live-search']").send_keys(conpanyname)  # 输入搜索内容
        driver.find_element_by_xpath("//div[@class='input-group-addon button-blue-sm pt0 pb0']").click()  # 点击搜索
        driver.implicitly_wait(10)

        # 选择相关度最高的搜索结果 第一条搜索框，然后再
        tag = driver.find_elements_by_xpath("//div[@class='search_right_item ml10']")
        if len(tag) == 0:
            print("没有查询到数据！！！第" + str(id) + "个【" + conpanyname + "】")
            conn_mysql.updateConpanyFlase(id);
            return 0;
        btn = tag[0].find_element_by_tag_name('a')
        print(btn);
        try:
            closeBtn = driver.find_element_by_id("bannerClose")
            if not closeBtn is None:
                closeBtn.click()
        except:
            print("")
        btn.click()
        driver.implicitly_wait(5)

        # 转化句柄
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                # 输出待选择的窗口句柄
                print(handle)
                driver.switch_to.window(handle)
        self.getData(driver, id);
        driver.close();
        driver.switch_to_window(all_handles[0])
        return driver

    def getData(self, driver, id):

        re = self.baseInfo("test", driver, id);
        print(re);
        conn_mysql.insertCompany(re);
        conn_mysql.updateConpany(id);
        return 1;

    def baseInfo(self, idd, driver, id):
        # base = self.driver.find_element_by_xpath("//div[@class='company_header_width ie9Style position-rel']/div")
        # # base '淘宝（中国）软件有限公司浏览40770\n高新企业\n电话：18768440137邮箱：暂无\n网址：http://www.atpanel.com
        # # 地址：杭州市余杭区五常街道荆丰村'
        # name = base.text.split('浏览')[0]
        # tel = base.text.split('电话：')[1].split('邮箱：')[0]
        # email = base.text.split('邮箱：')[1].split('\n')[0]
        # web = base.text.split('网址：')[1].split('地址')[0]
        # address = base.text.split('地址：')[1]
        # abstract = self.driver.find_element_by_xpath("//div[@class='sec-c2 over-hide']//script")
        # # 获取隐藏内容
        # abstract = self.driver.execute_script("return arguments[0].textContent", abstract).strip()
        cname = driver.find_element_by_xpath(
            "//div[@class='position-rel']/span[@class='f18 in-block vertival-middle sec-c2']").text
        pname = driver.find_element_by_xpath(
            "//div[@class='f18 overflow-width sec-c3']/a").text
        tabs = driver.find_elements_by_tag_name('table')
        rows = tabs[1].find_elements_by_tag_name('tr')
        cols = rows[0].find_elements_by_tag_name('td' and 'th')
        # 工商注册号
        reg_code = rows[0].find_elements_by_tag_name('td')[1].text
        # 注册地址
        reg_address = rows[5].find_elements_by_tag_name('td')[1].text
        # 英文名称
        # english_name = rows[5].find_elements_by_tag_name('td')[1].text
        # 经营范围
        # ent_range = rows[6].find_elements_by_tag_name('td')[1].text
        # 统一信用代码
        creditcode = rows[1].find_elements_by_tag_name('td')[1].text
        # 纳税人识别号
        tax_code = rows[2].find_elements_by_tag_name('td')[1].text
        # 营业期限
        # deadline = rows[3].find_elements_by_tag_name('td')[1].text
        # 企业类型
        # ent_type = rows[1].find_elements_by_tag_name('td')[3].text

        # baseInfo = (idd, name, tel, email, web, address, abstract, reg_code, reg_address, english_name, ent_range,
        #             creditcode, tax_code, deadline, ent_type)

        return (id, cname, pname, reg_code, creditcode, reg_address, tax_code)
