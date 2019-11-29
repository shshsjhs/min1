import requests
r=requests.get("https://www.baidu.com")

print(r.encoding)

print(r.apparent_encoding)

r.encoding='utf-8'
print(r.text)
