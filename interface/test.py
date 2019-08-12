# -*- coding: UTF-8 -*-
# from interface.inter import HTTP
# import inspect
# from common import config


# http = HTTP()
# http.post('http://112.74.191.10/inter/HTTP/auth')
# http.assertequals('status', '200')
# http.savejson('token', 't')
# http.addheader('token', '{t}')
#
# http.post('http://112.74.191.10/inter/HTTP/login', d="username=Roy&password=123456")
# http.assertequals('status', '200')
#
# http.savejson('userid','userid')
# http.post('http://112.74.191.10/inter/HTTP/getUserInfo', d="id={userid}")
# http.assertequals('status', '200')
#
# http.post('http://112.74.191.10/inter/HTTP/logout')
# http.assertequals('status', '200')


# http = HTTP()
# func = getattr(http, 'post')
# func('http://112.74.191.10/inter/HTTP/auth')
# args = inspect.getfullargspec(func).__str__()
# print(args)
# args = args[args.find('args=')+5:args.rfind(', varargs')]
# args = eval(args)
# args.remove('self')
# print(len(args))

# config.get_config('../lib/conf.properties')
# print(config.config)

# import json,jsonpath
#
# s = '{"status":"0","t":"1565613956798","set_cache_time":"","data":[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.1.1.1","origipquery":"1.1.1.1","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"1.1.1.1","tplt":"ip","resourceid":"6006","fetchkey":"1.1.1.1","appinfo":"","role_id":0,"disp_type":0}]}'
# jsons = json.loads(s)
# res = jsonpath.jsonpath(jsons,'status')[0]
# print(res)

import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

