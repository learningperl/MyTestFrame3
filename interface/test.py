# -*- coding: UTF-8 -*-
from interface.inter import HTTP


http = HTTP()
http.post('http://112.74.191.10/inter/HTTP/auth')
http.assertequals('status', '200')
http.savejson('token', 't')
http.addheader('token', '{t}')

http.post('http://112.74.191.10/inter/HTTP/login', d="username=Roy&password=123456")
http.assertequals('status', '200')

http.savejson('userid','userid')
http.post('http://112.74.191.10/inter/HTTP/getUserInfo', d="id={userid}")
http.assertequals('status', '200')

http.post('http://112.74.191.10/inter/HTTP/logout')
http.assertequals('status', '200')