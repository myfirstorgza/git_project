import urllib.request

import pymysql
from bs4 import BeautifulSoup
from jupyter_server.auth import passwd

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='0319',
                             database='spider2202_douban',
                             cursorclass=pymysql.cursors.DictCursor)



h={"user-agent":"Mozilla/5.0(Windows NT 10.0;win64;x64)"
                "AppleWebKit/537.36(KHTML,like Gecko)Chrome/128.0.0.0 Safari/537.36"}  #键值对
req= urllib.request.Request("https://movie.douban.com/top250",headers=h)

r=urllib.request.urlopen(req) #传Request对象

#使用常规获取
#print(r.read().decode())

#使用bs4库获取item
soup=BeautifulSoup(r.read().decode(),'html.parser')

items =soup.find_all("div",class_="item")

#print(items)
with connection:
  for item in items:
      pic_div =item.find("div",class_="pic")
      img = pic_div.a.img
      name = img['alt']
      url = img['src']
    #print(img['alt'])
   #print(img['src'])
      with connection.cursor() as cursor:
             sql = "INSERT INTO `movie_info`(`movie_name`,`movie_url`) VALUES (%s,%s)"
             cursor.execute(sql,(name,url))
  connection.commit()
