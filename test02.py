import requests

import test02

headers={
    "Accept": "application/json",
     "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",}

proxies = {"http":"http://180.88.111.187:3128",
           "https":"http://180.88.111.187:3128"}


r = requests.get('http://httpbin.org/get',headers=headers,proxies=proxies)

print(r.text)