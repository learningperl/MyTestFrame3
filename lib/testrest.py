# -*- coding: UTF-8 -*-
import requests



session = requests.session()
res = session.post('http://112.74.191.10/inter/REST/user/register/%7B%22name%22:%22ttttttt%22,%22pwd%22:%22ttttttt%22,%22nickname%22:%22tttttt%22,%22describe%22:%22tttttt%22%7D')
print(res)



