# -*- coding: UTF-8 -*-
from web.Web import Browser
import time
import traceback

# 启动浏览器
driver = Browser()
driver.openbrowser()
driver.get('http://112.74.191.10:8000/')


# 登录页面
def login(driver):
    # 点击登录
    driver.click('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
    # 输入用户
    driver.input('//*[@id="username"]', '13800138006')
    # 输入密码
    driver.input('//*[@id="password"]','123456')
    # 输入验证码
    driver.input('//*[@id="verify_code"]','11111')
    # 点击登录
    driver.click('//*[@id="loginform"]/div/div[6]/a')
    time.sleep(3)
    # 获取退出登录的文本
    driver.gettext('/html/body/div[1]/div/div/div/div[2]/a[2]')
    # 校验登录是否成功
    if driver.text == '安全退出':
        print('PASS')
    else:
        print('FAIL')

# 个人中心
def userinfo(driver):
    driver.click('/html/body/div[3]/div/div[2]/div[1]/div/ul[4]/li[2]/a')
    driver.click('//*[@id="preview"]')
    driver.intoiframe('//*[@id="layui-layer-iframe1"]')
    driver.input('//*[@id="filePicker"]/div[2]/input','C:\\Users\\Will\\Desktop\\1.png')
    driver.outiframe()
    driver.click('//*[@id="layui-layer1"]/span[1]/a[3]')

    driver.click('/html/body/div[1]/div/div/ul/li[5]/a')
    driver.switchwindow(1)
    driver.gettitle()
    print(driver.title)
    driver.closewindow()
    driver.switchwindow(0)

# 搜索
def search(driver):
    driver.input('//*[@id="q"]','手机')
    driver.click('//*[@id="sourch_form"]/a')
    driver.moveto('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[4]/a')
    driver.click('/html/body/div[4]/div/div[2]/div[2]/ul/li[10]/div/div[5]/div[2]/a')
    driver.click('//*[@id="layui-layer1"]/span/a')
    driver.excutejs('window.scrollBy(0,800)')
    driver.excutejs('return window.HTMLTitleElement.name')
    print(driver.jsres)

# 购物车
def cart(driver):
    driver.click('//*[@id="hd-my-cart"]/a/div')
    driver.click('/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/a')

# 提交订单
def order(driver):
    time.sleep(3)
    driver.click('/html/body/div[14]/div/button')


login(driver)
# userinfo(driver)
search(driver)
cart(driver)
order(driver)

time.sleep(5)
driver.quit()
