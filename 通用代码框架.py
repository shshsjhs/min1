import requests

def HTML(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"
        
#if __name__=="__mian__":
url=input()
print (HTML(url))