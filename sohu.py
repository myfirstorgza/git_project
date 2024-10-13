import urllib.request

r = urllib.request.urlopen("http://www.sohu.com/")
print(r.status)
print(r.msg)
print(r.read().decode())