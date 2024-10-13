import urllib.request

r = urllib.request.urlopen("http://httpbin.org/get")

print(r.read().decode())