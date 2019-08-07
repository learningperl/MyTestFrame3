# -*- coding: UTF-8 -*-
import requests, json, traceback


class HTTP:
    """
        这是HTTP接口自动化的关键字库
        powered by william
        at: 2019/08/05
    """

    def __init__(self, writer):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
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
            self.writer.write(self.writer.row, 7,'PASS')
            self.writer.write(self.writer.row, 8, self.url)
        else:
            print('error：url格式错误')
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

        if d is None or d == '':
            pass
        else:
            d = self.__get_param(d)
            d = self.__get_data(d)

        # 如果请求https请求，报ssl错误，就添加verify=False参数
        res = self.session.post(url, d, j, verify=False)
        self.result = res.content.decode('utf8')
        print(self.result)
        try:
            self.jsonres = json.loads(self.result)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
        except Exception as e:
            # 异常处理的时候，分析逻辑问题
            self.jsonres = {}
            self.writer.write(self.writer.row, 7, 'FAIL')
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
            print('没有' + key + '这个键的header存在')
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

    def assertequals(self, key, value):
        """
        断言json结果里面，某个键的值和value相等
        :param key: json结果的键
        :param value: 预期的值
        :return: 无
        """
        value = self.__get_param(value)
        res = str(self.result)
        try:
            res = str(self.jsonres[key])
        except Exception as e:
            pass

        if res == str(value):
            print('PASS')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, res)
        else:
            print('FAIL')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际：' + res +'  预期结果：' + value)

    def savejson(self, key, p):
        """
        将需要保存数据，保存为参数p的值
        :param key: 需要保存的json的键
        :param p: 保存后，调用参数的参数名字{p}
        :return: 无
        """
        try:
            self.params[p] = self.jsonres[key]
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            print("error：保存参数失败！没有" + key + "这个键。")
            print(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))

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
