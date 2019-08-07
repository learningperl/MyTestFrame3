# -*- coding: UTF-8 -*-
from interface.inter import HTTP
import inspect


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


http = HTTP()
func = getattr(http, 'post')
func('http://112.74.191.10/inter/HTTP/auth')
args = inspect.getfullargspec(func).__str__()
print(args)
args = args[args.find('args=')+5:args.rfind(', varargs')]
args = eval(args)
args.remove('self')
print(len(args))



