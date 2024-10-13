import test02

headers={
    "Accept": "application/json",
     "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",}

proxies = {"http":"http://153.101.67.170:9002",
           "https":"http://153.101.67.170:9002"}

data = {'username':'longmao',
        'password':'123456'}
r = requests.post('http://httpbin.org/post',headers=headers,proxies=proxies,data=data)

print(r.text)