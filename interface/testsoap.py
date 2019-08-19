# -*- coding: UTF-8 -*-
from suds.client import Client
from suds.xsd.doctor import Import,ImportDoctor
import json


# # 通过wsdl解析出当前webservice服务提供的接口
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
# # 可以通过webservice服务的client对象去调用服务
# res = client.service.auth()
# jsonres = json.loads(res)
# print(res)
# # 往client里面添加头，解决头部关联问题
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers={'token':jsonres['token']})
# res = client.service.login('will','123456')
# print(res)
# res = client.service.getUserInfo(1)
# print(res)
# res = client.service.logout()
# print(res)



# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
# # 可以通过webservice服务的client对象去调用服务
# res = client.service.__getattr__('auth')()
# jsonres = json.loads(res)
# print(res)
# # 往client里面添加头，解决头部关联问题
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers={'token':jsonres['token']})
# params = "Will、123456"
# paramslist = params.split('、')
# res = client.service.login(*paramslist)
# print(res)
# res = client.service.getUserInfo(1)
# print(res)
# res = client.service.logout()
# print(res)


imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# 指定命名空间
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)
client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)
# 可以通过webservice服务的client对象去调用服务
res = client.service.__getattr__('getSupportCity')('湖南')
print(res)