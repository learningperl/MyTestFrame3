# -*- coding: UTF-8 -*-
from selenium.webdriver import *
import time, os, traceback
from selenium.webdriver.common.action_chains import ActionChains


# 用类封装打开浏览器的方法
class Browser:

    def __init__(self,writer):
        # 保存打开的浏览器
        self.writer = writer
        self.driver = None
        self.text = ''
        self.title = ''
        self.jsres = ''

    # 定义打开浏览器的函数
    def openbrowser(self, b='gc', dr=None):
        # 打开谷歌浏览器
        if b == 'gc' or b == '':
            if dr is None or dr == '':
                dr = './web/lib/chromedriver'
            # 创建一个用来配置chrome属性的变量
            option = ChromeOptions()
            option.add_argument('--disable-infobars')
            # 添加用户文件，使用浏览器缓存，可以提升加载速度
            # will的用户目录C:\Users\Will\AppData\Local\Google\Chrome\User Data
            # 添加用户配置文件，可以带缓存
            # 代码自动化获取用户目录
            userdir = os.environ['USERPROFILE'] + "\\AppData\\\Local\\\Google\\\Chrome\\User Data"
            option.add_argument('--user-data-dir=' + userdir)
            # self.driver.switch_to.frame(self.driver.find_element_by_xpath(''))
            # 打开谷歌浏览器
            self.driver = Chrome(executable_path=dr, options=option)
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
            # self.driver.window_handles
        # 打开ie
        elif b == 'ie':
            if dr is None or dr == '':
                dr = './web/lib/IEDriverServer'
            self.driver = Ie(executable_path=dr)
            self.driver.implicitly_wait(30)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        # 打开火狐
        elif b == 'ff':
            if dr is None or dr == '':
                dr = './web/lib/geckodriver'
            self.driver = Firefox(executable_path=dr)
            self.driver.implicitly_wait(30)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        else:
            print('暂未实现该浏览器代码！')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '暂未实现该浏览器代码')

    # 访问网站
    def get(self, url):
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, url)
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def input(self,xpath,value):
        self.driver.find_element_by_xpath(xpath).send_keys(str(value))
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def intoiframe(self,xpath):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def outiframe(self):
        self.driver.switch_to.default_content()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def sleep(self,t=3):
        time.sleep(int(t))
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')


    def gettext(self,xpath):
        self.text = self.driver.find_element_by_xpath(xpath).text
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def gettitle(self):
        self.title = self.driver.title
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def switchwindow(self,idx=0):
        h = self.driver.window_handles
        self.driver.switch_to.window(h[int(idx)])
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def closewindow(self):
        # 关闭selenium当前定位的窗口
        self.driver.close()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def moveto(self,xpath):
        actions = ActionChains(self.driver)
        ele = self.driver.find_element_by_xpath(xpath)
        actions.move_to_element(ele).perform()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def excutejs(self,js):
        self.jsres = self.driver.execute_script(js)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def assertequals(self,p,value):
        try:
            p = p.replace('{text}',self.text)
            p = p.replace('{jsres}',self.jsres)
            p = p.replace('{title}',self.title)
            if str(p) == str(value):
                self.writer.write(self.writer.row, 7, 'PASS')
                self.writer.write(self.writer.row, 8, '')
            else:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(p))
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))