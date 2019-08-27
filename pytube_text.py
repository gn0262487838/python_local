

from selenium.webdriver import Chrome
from pytube import Playlist
import time
import os
driver = Chrome("./Chromedriver")
driver.get("https://www.youtube.com/user/boyceavenue/playlists")

# find find_element 找一個
# find_all find_elements 找多個

# 登入google
# driver.find_element_by_id("identifierId").send_keys("")
# driver.find_element_by_id("identifierNext").click()
# time.sleep(1)
# driver.find_element_by_name("password").send_keys("")
# driver.find_element_by_id("passwordNext").click()
# time.sleep(10)

# 拿紙條  bs4:.text ; selenium: .text 
# 拿標籤  bs4:["href"] ; selenium: get_attribute("href")

na = driver.find_elements_by_id("video-title")

# for i in na: 先做一個測試
title = na[0].text
url = na[0].get_attribute("href")
print(title, url)

pl = Playlist(url,suppress_exception=True)  # suppress_exception表示如果下載檔案中有發生檔案遺失(比較久的檔案)，請電腦忽視此問題繼續下載剩下的影像。
    
dirname = "youtubelist/"
if not os.path.exists(dirname):
    os.mkdir(dirname)
pl.download_all(dirname)    #依然卡到keyerror: "title"???

time.sleep(60)
driver.close()



