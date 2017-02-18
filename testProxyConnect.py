import requests as r
import random
from bs4 import BeautifulSoup as bs

ipList = []
with open("E:/ips.txt","r") as f:
    for item in f.readlines():
        ipList.append(item)
    f.close()

baseUrl = "http://www.j4.com.tw/james/remoip/"
for i in range(0,10):
    nip = random.randint(0, len(ipList) - 1)
    ip = ipList.__getitem__(nip).strip()
    # proxy = {"http": "http://{}".format(ip)}
    proxy = {"http": "http://127.0.0.1:8118"}

    n = 0
    while True:
        try:
            if n >= 5:
                print("http not found !!")
                exit
            res = r.get(baseUrl, proxies=proxy, timeout=6)
            # res = r.get(baseUrl, timeout=6)
            if res.status_code == 200 and res.text.strip() != u"HTTP/1.1 400 Bad Request":
                break
        except:
            n += 1
            nip = random.randint(0, len(ipList) - 1)
            ip = ipList.__getitem__(nip).strip()
            proxy = {"http": "http://{}".format(ip)}
            pass
    print res.text

