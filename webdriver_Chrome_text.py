
from selenium.webdriver import Chrome
import time
#使用selenium import webdriver chrome時需把driver下載下來後解壓縮出chromedriver.exe，此時記得要把此檔放進去專案資料夾喔!!!
driver = Chrome("./Chromedriver")
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#find >>> find_element 找一個
#find_all >>> find_elements 找多個
driver.find_element_by_id("identifierId").send_keys("...")
driver.find_element_by_id("identifierNext").click()
time.sleep(1)
driver.find_element_by_name("password").send_keys("...")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

# 拿紙條  bs4:.text ; selenium: .text 
# 拿標籤  bs4:["href"],另一種方式是ex. find("a").attrs["href"] ; selenium: get_attribute




