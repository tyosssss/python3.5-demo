# -*- coding:utf-8 -*-
import requests
url = 'https://m.wingontravel.com'
res = requests.get(url)

print(res.text)

