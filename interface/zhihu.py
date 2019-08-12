# -*- coding: UTF-8 -*-
import requests,json


session = requests.session()
requests.packages.urllib3.disable_warnings()
session.headers['content-type'] = 'application/x-www-form-urlencoded'
session.headers[
    'user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
session.headers['x-zse-83'] = '3_2.0'

res = session.post('https://www.zhihu.com/udid')
print(res.text)

print(session.cookies)
res = session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn')
print(res.text)

# 登录
res = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
                   data='aR79k4U0cT2tXqYq8LPG6vHmxq2pkLnmtbSBDgg9kLtxgeSmhbfGiqX1jbfVoG398LF0gQN0cT2tuqYq8LkMQbwGivwOgUxGw9e0g4e8kCV92vgBzh3qk4R92LkYFhVGwqoVJbCGST2tEqx9BLkBEJXmST2tXqYhZUS8eDC8FBtxg7Fqm4O8nCL8DU3m2LPB8vSG2gC8QBtxg_VBXbP1UvLKQ_2pkLkBXgxGEJeGsgHm2LfBpwNmkveMcBtxg8F0hhNBUguqg9OpQXOq8Mtqo6LyNhOpQRF0ZqO8nvr0bXtf20Y0Tut924_BkC3VUbSBtq3qk478gGpucUO1PD3ZJCe8Xq2tgqNMsvSMS79hS02xoTF0MXFqcQ9qr_LxgRVmZ9oMgGL1eBtxg_NMwGoM2JXMXq2tguVKKvwGEJHM3BtxgRF0zuFqrH9BrXxpggY8BTxyNguq6X2fS828G8OBFgr8Xq2tHgSVKbOBDBe8',
                   verify=False)
print(res.text)
