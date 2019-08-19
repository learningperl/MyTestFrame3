# # This sample code uses the Appium python client
# # pip install Appium-Python-Client
# # Then you can paste this into a file and simply run with Python
#
# from appium import webdriver
#
# caps = {}
# caps["platformName"] = "Android"
# caps["platformVersion"] = "7.1.2"
# caps["deviceName"] = "8c4ec53b"
# caps["appPackage"] = "com.tencent.mobileqq"
# caps["appActivity"] = ".activity.SplashActivity"
# caps["noReset"] = "true"
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# driver.implicitly_wait(20)
#
# # 登录界面
# el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
# el1.clear()
# el1.send_keys("3599292078")
# el5 = driver.find_element_by_accessibility_id("密码 安全")
# el5.clear()
# el5.send_keys("xiaobao168")
# el6 = driver.find_element_by_accessibility_id("登 录")
# el6.click()
#
# # 设置界面
# el7 = driver.find_element_by_accessibility_id("帐户及设置")
# el7.click()
# el8 = driver.find_element_by_accessibility_id("设置")
# el8.click()
# el9 = driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
# el9.click()
# el10 = driver.find_element_by_accessibility_id("退出当前帐号按钮")
# el10.click()
# el11 = driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
# el11.click()
#
# driver.quit()


# import os,threading,time
# def run():
#     os.popen('node E:\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js -p 4724').read()
#
#
# th = threading.Thread(target=run, args=())
# th.start()
# print(11111)
# time.sleep(15)
# print(22222)


# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "8c4ec53b"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["noReset"] = "true"
caps["unicodeKeyboard"] = "true"
caps["resetKeyboard"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(20)

time.sleep(15)
TouchAction(driver).press(x=360, y=281).move_to(x=376, y=927).release().perform()

el1 = driver.find_element_by_xpath(
    "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout")
el1.click()
time.sleep(15)

el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout")
el2.click()
time.sleep(2)
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View")
time.sleep(2)
el3.click()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View")
el4.send_keys("手机")
el5 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View")
el5.click()
el6 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[5]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]")
el6.click()

driver.quit()