# -*- coding: UTF-8 -*-
import requests, json, traceback


class HTTP:
    """
        这是HTTP接口自动化的关键字库
        powered by william
        at: 2019/08/05
    """

    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
        self.result = ''
        self.jsonres = {}
        # 用来保存关联数据的字段
        self.params = {}

    def post(self, url, d=None, j=None, en='utf8'):
        if d is None:
            pass
        else:
            d = self.__get_param(d)
            d = self.__get_data(d)

        # 如果请求https请求，报ssl错误，就添加verify=False参数
        res = self.session.post(url, d, j, verify=False)
        self.result = res.content.decode(en)
        try:
            self.jsonres = json.loads(self.result)
        except Exception as e:
            # 异常处理的时候，分析逻辑问题
            self.jsonres = {}

    def addheader(self, key, value):
        value = self.__get_param(value)
        self.session.headers[key] = value

    def assertequals(self, key, value):
        res = str(self.result)
        try:
            res = str(self.jsonres[key])
        except Exception as e:
            pass

        if res == str(value):
            print('PASS')
        else:
            print('FAIL')

    def savejson(self, key, p):
        # 将需要保存数据，保存为参数p的值
        try:
            self.params[p] = self.jsonres[key]
        except Exception as e:
            print("error：保存参数失败！没有" + key + "这个键。")
            print(traceback.format_exc())

    def __get_param(self, s):
        # 按规则获取关联的参数
        # 遍历已经保存的参数，并将传入字符串里面，满足{key}所有字符串用key的值来替换
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s

    def __get_data(self, s):
        # s = eval(s)
        # return s
        # 分离键值对
        param = {}
        p = s.split('&')
        # 获取键和值
        # username=Roy&password
        for pp in p:
            # 分离键和值
            ppp = pp.split('=')
            # 异常处理
            try:
                param[ppp[0]] = ppp[1]
            except Exception as e:
                print('error：URL参数格式不标准！')
                print(traceback.format_exc())

        # print(param)
        return param
