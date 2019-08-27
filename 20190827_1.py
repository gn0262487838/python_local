# -*- utf-8 -*- #
from bs4 import BeautifulSoup 
import requests
import prettytable
url = "https://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1566803524459"

response = requests.get(url)
# 告訴回應編碼是utf8
response.encoding = "utf8"
html = BeautifulSoup(response.text)

lis = html.find("div",style="width:670px; border:0px red solid; overflow:hidden; padding:0 0 0 20px;")

pt = prettytable.PrettyTable()
c = []
t = []
p = []
for i in lis.find_all("td",width="60%"):
    c.append(i.find("a").text)
for i in lis.find_all("td",width="50%"):
    t.append(i.find("a").text)
for i in lis.find_all("td",width="18%"):
    p.append(i.find("a").text)

pt.add_column("城市",c)
pt.add_column("溫度",t)
pt.add_column("降雨機率",p)
print(pt)




    



    
    
