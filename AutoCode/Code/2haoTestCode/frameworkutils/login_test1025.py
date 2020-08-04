import json
import time
from urllib import parse

import requests
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
driver.find_element_by_xpath("//a[text()='登录']")
driver.find_element_by_name("userName").send_keys("1356046")
driver.find_element_by_name("userName").send_keys("x9122")
driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']").click()

cookies = driver.get_cookies()
print (type(cookies))
# print ("".join(cookies))
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close

f1 = open('cookie.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
# # 刷新页面
driver.refresh()
