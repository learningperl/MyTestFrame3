# -*- coding: UTF-8 -*-
from appium import webdriver
from common import logger
import traceback, os, time, threading


class APP:
    """
        这是APP自动化的关键字库
        powered by william
        at: 2019/08/19
    """

    def __init__(self, writer):
        self.driver = None
        self.t = 20
        self.port = '4723'
        self.writer = writer

    def runappium(self, path='', port='', t=''):
        """
        启动appium服务
        :path：appium的安装路径
        :param port: 服务的启动端口
        :t：等待时间
        :return:
        """
        try:
            if path == '':
                cmd = 'node E:\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            else:
                cmd = 'node ' + path + '\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            if port == '':
                cmd += ' -p 4723'
            else:
                self.port = port
                cmd += ' -p ' + port

            if t == '':
                t = 5
            else:
                t = int(t)

            # 启动appium服务
            def run(cmd):
                try:
                    os.popen(cmd).read()
                except Exception as e:
                    pass

            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(t)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def runapp(self, conf, t=''):
        """
        连接appium服务器，并根据conf配置，启动待测试APP
        :param conf: APP的启动配置，为标准json字符串
        :param t:
        :return:
        """
        try:
            conf = eval(conf)
            if t == '':
                t = 20
            else:
                t = int(t)
            self.t = t
            self.driver = webdriver.Remote('http://127.0.0.1:' + self.port + '/wd/hub', conf)
            self.driver.implicitly_wait(t)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
            # self.driver.fid
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def __findele(self, path):
        """
        定位元素
        :param path: 元素的定位路径，支持accessibility_id，id，xpath
        :return: 找到的元素，如没找到，就返回None
        """
        ele = None
        try:
            if path.startswith('/'):
                # xpath定位
                ele = self.driver.find_element_by_xpath(path)
            else:
                try:
                    # 优先去看accessibility_id定位
                    self.driver.implicitly_wait(5)
                    ele = self.driver.find_element_by_accessibility_id(path)
                except Exception as e:
                    # 如果不是accessibility_id，就用id定位
                    self.driver.implicitly_wait(self.t)
                    ele = self.driver.find_element_by_id(path)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

        return ele

    def click(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error('No such element:' + path)
        else:
            try:
                ele.click()
                self.writer.write(self.writer.row, 7, 'PASS')
            except Exception as e:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def clear(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error('No such element:' + path)
        else:
            try:
                ele.clear()
                self.writer.write(self.writer.row, 7, 'PASS')
            except Exception as e:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def input(self, path, text):
        ele = self.__findele(path)
        if ele is None:
            logger.error('No such element:' + path)
        else:
            try:
                ele.clear()
                ele.send_keys(text)
                self.writer.write(self.writer.row, 7, 'PASS')
            except Exception as e:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def closeappium(self):
        try:
            os.popen('taskkill /F /IM node.exe')
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def quit(self):
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
