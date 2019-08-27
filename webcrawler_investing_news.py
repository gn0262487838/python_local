import requests
# 此處並非使用Requests，因為requests.get()會暫時幫你帶入簡單的user-agent，但investing.com比較嚴格，
# 故須回到urllib.request引入Request並加上.add_header("user-agent","...")
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

df_news = pd.DataFrame(columns=["標題","發布時間","新聞網址"])
page = 0
while True:
    url = "https://www.investing.com/news/world-news"+"/"+str(page)
    page += 1
    r = Request(url)
    r.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
    response = urlopen(r)
    html = BeautifulSoup(response)

    html_new = html.find("div",class_="largeTitle")

    for i in html_new.find_all("article",class_="js-article-item"):
        cont = i.find("a",class_="title")
        try:
            tim = i.find("span",class_="date").text
        except:
            tim = "None"
        print("標題", cont.text)
        print("發布時間:", tim)
        urll ="網址:https://www.investing.com" + cont["href"]
        print(urll)
        S = pd.Series([cont.text, tim, urll],
                index=["標題","發布時間","新聞網址"]
                )
        df_news = df_news.append(S,ignore_index=True)   #df_news.append(S,ignore_index=True)只是做操作，記得還要丟回去df_news!!!

    df_news.to_csv("investing_news.csv",encoding="utf-8",index=0)   #放在此，即每完成一頁，就要存檔一次，免得全部跑完再存檔不知道要跑多久!!!






    

