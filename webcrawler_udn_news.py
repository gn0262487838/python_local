# -*- utf-8 -*- #
from bs4 import BeautifulSoup
import requests
import pymysql

# Start #

# 連接資料庫
udn_news = pymysql.connect(
host = "localhost",
user = "root",
passwd = "",
db = "udn_news",
charset = "utf8"
)
# 獲得操作游標
cmd = udn_news.cursor()

# 抓取udn news
url = "https://udn.com/news/breaknews/1"

response = requests.get(url)
html = BeautifulSoup(response.text)

cont_1 = html.find("div", {
    "id":"breaknews_body"
})

cont_2 = cont_1.find("dl").find_all("dt")
for i in cont_2:
    z = i.find("h2")
    if z != None:
        # 文章標題
        title = z.find("a").text
        # 內文連結
        URL = z.find("a").attrs["href"]
        # 內容
        url_n = "https://udn.com" + z.find("a").attrs["href"]
        r = requests.get(url_n)
        cont_n = BeautifulSoup(r.text)
        txt = ""
        for j in cont_n.find("div", id = "story_body_content").find_all("p"):
            txt  += j.text    
        # insert into sql 
        cmd.execute(
            "insert into `udn_news`(`url`,`title`,`content`) value(%s,%s,%s)"
            ,(URL, title, txt))
        udn_news.commit()

# disconncet
udn_news.close()

# over #