# -*- coding: UTF-8 -*-
import requests, json, jsonpath,traceback
from common import logger
from suds.client import Client
from suds.xsd.doctor import Import,ImportDoctor


class HTTP:
    """
        这是HTTP接口自动化的关键字库
        powered by william
        at: 2019/08/05
    """

    def __init__(self, writer):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
        self.session.headers['content-type'] = 'application/x-www-form-urlencoded'
        self.session.headers[
            'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        self.result = ''
        self.jsonres = {}
        # 用来保存关联数据的字段
        self.params = {}
        self.url = ''
        self.writer = writer

    def seturl(self, u):
        """
        设置请求的url host地址
        :param u: url的host地址
        :return: 无
        """
        if u.startswith('http') or u.startswith('https'):
            self.url = u
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, self.url)
        else:
            logger.error('url格式错误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'url格式错误')

    def post(self, url, d=None, j=None):
        """
        发送post请求
        :param url: url路径，可以是单纯的路径+全局的host。也可以是http/https开头的绝对路径
        :param d: 标准url data传参
        :param j: 传递json字符串的参数
        :return: 无
        """
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url + '/' + url

        d = self.__get_param(d)

        if d is None or d == '':
            pass
        else:
            if d.__contains__('='):
                d = self.__get_data(d)

        # 如果请求https请求，报ssl错误，就添加verify=False参数
        print(d)
        res = self.session.post(url, d, j, verify=False)
        self.result = res.content.decode('UTF-8')
        logger.info(self.result)
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
        except Exception as e:
            # 异常处理的时候，分析逻辑问题
            self.jsonres = {}
            # logger.exception(e)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.result))

    def get(self, url, params=None):
        """
        发送post请求
        :param url: url路径，可以是单纯的路径+全局的host。也可以是http/https开头的绝对路径
        :param d: 标准url data传参
        :param j: 传递json字符串的参数
        :return: 无
        """
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url + '/' + url + "?" + params
        else:
            url = url + "?" + params

        # 如果请求https请求，报ssl错误，就添加verify=False参数
        res = self.session.get(url, verify=False)
        self.result = res.content.decode('utf8')
        logger.info(self.result)
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(jsons))
        except Exception as e:
            # 异常处理的时候，分析逻辑问题
            self.jsonres = {}
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.result))

    def removeheader(self, key):
        """
        从头里面删除一个键值对
        :param key: 要删除的键
        :return: 无
        """
        try:
            self.session.headers.pop(key)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
        except Exception as e:
            logger.error('没有' + key + '这个键的header存在')
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))

    def addheader(self, key, value):
        """
        添加一个键值对，支持关联
        :param key: 要添加的键
        :param value: 键的值
        :return: 无
        """
        value = self.__get_param(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.session.headers))

    def assertequals(self, jpath, value):
        """
        断言json结果里面，某个键的值和value相等
        :param key: json结果的键
        :param value: 预期的值
        :return: 无
        """
        value = self.__get_param(value)
        if value == 'None':
            value = None
        res = str(self.result)
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jpath)[0])
        except Exception as e:
            res = None
            pass

        if res == value:
            logger.info('PASS')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, res)
        else:
            logger.info('FAIL')
            self.writer.write(self.writer.row, 7, 'FAIL')
            if res is None:
                res = 'None'
            if value is None:
                value = 'None'
            self.writer.write(self.writer.row, 8, '实际：' + res + '  预期结果：' + value)

    def savejson(self, jpath, p):
        """
        将需要保存数据，保存为参数p的值
        :param key: 需要保存的json的键
        :param p: 保存后，调用参数的参数名字{p}
        :return: 无
        """
        try:
            self.params[p] = str(jsonpath.jsonpath(self.jsonres, jpath)[0])
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            logger.error("保存参数失败！没有" + jpath + "这个键。")
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))

    def __get_param(self, s):
        # 按规则获取关联的参数
        # 遍历已经保存的参数，并将传入字符串里面，满足{key}所有字符串用key的值来替换
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s

    def __get_data(self, s):
        # 默认是标准的url参数
        flg = False
        # s = eval(s)
        # return s
        # 分离键值对
        param = {}
        p = s.split('&')
        # 获取键和值
        # username=Roy&password
        for pp in p:
            param[pp[0:pp.find('=')]] = pp[pp.find('=')+1:]

        # print(param)
        if flg:
            s = s.encode('utf-8')
            return s
        else:
            return param


class SOAP:
    """
        这是HWebservice接口自动化的关键字库
        powered by william
        at: 2019/08/14
    """

    def __init__(self, writer):
        # 定义wsdl描述文档的地址
        self.wsdl = ''
        self.client = None
        self.result = ''
        self.jsonres = {}
        self.writer = writer
        self.headers = {}
        self.params = {}
        self.doctor = None

    # 设置wsdl路径，并解析webservice服务
    def setwsdl(self, url):
        self.wsdl = url
        self.client = Client(url,doctor=self.doctor)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, self.wsdl)
        return True

    def adddoctor(self,s=None,x=None,n=None):
        imp = Import(s, location=x)
        # 指定命名空间
        imp.filter.add(n)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')
        return True

    def callmethod(self, m, l=None):
        # 调用服务，并获得接口返回值
        if l == None or l == '':
            try:
                self.result = self.client.service.__getattr__(m)()
            except Exception as e:
                self.result = e.__str__()
                print(self.result)
        else:
            l = l.split('、')
            for i in range(len(l)):
                l[i] = self.__get_param(l[i])
                if l[i] == 'None':
                    l[i] = None
            try:
                self.result = self.client.service.__getattr__(m)(*l)
            except Exception as e:
                self.result = e.__str__()

        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
        except Exception as e:
            # 异常处理的时候，分析逻辑问题
            self.jsonres = {}
            logger.exception(e)
            print(str(traceback.format_exc()))
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.result))

        return True

    # 添加头
    def addheader(self, key, value):
        value = self.__get_param(value)
        self.headers[key] = value
        self.client = Client(self.wsdl, headers=self.headers)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.result))
        return True

    def removeheader(self, key):
        self.headers.pop(key)
        self.client = Client(self.wsdl, headers=self.headers)
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.result))
        return True

    def savejson(self, jpath, p):
        """
        将需要保存数据，保存为参数p的值
        :param key: 需要保存的json的键
        :param p: 保存后，调用参数的参数名字{p}
        :return: 无
        """
        try:
            self.params[p] = str(jsonpath.jsonpath(self.jsonres, jpath)[0])
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
            return True
        except Exception as e:
            logger.error("保存参数失败！没有" + jpath + "这个键。")
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            return False

    def assertequals(self, jpath, value):
        """
        断言json结果里面，某个键的值和value相等
        :param key: json结果的键
        :param value: 预期的值
        :return: 无
        """
        value = self.__get_param(value)
        if value == 'None':
            value = None
        res = str(self.result)
        try:
            res = str(jsonpath.jsonpath(self.jsonres, jpath)[0])
        except Exception as e:
            res = None
            pass

        if res == value:
            logger.info('PASS')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, res)
            return True
        else:
            logger.info('FAIL')
            self.writer.write(self.writer.row, 7, 'FAIL')
            if res is None:
                res = 'None'
            if value is None:
                value = 'None'
            self.writer.write(self.writer.row, 8, '实际：' + res + '  预期结果：' + value)
            return False

    def __get_param(self, s):
        # 按规则获取关联的参数
        # 遍历已经保存的参数，并将传入字符串里面，满足{key}所有字符串用key的值来替换
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s
