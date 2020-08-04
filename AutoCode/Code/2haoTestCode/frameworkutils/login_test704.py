
from urllib import parse

import requests
from pywin.tools import browser
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://i.2haohr.com/desk")
cookies=driver.get_cookies()
print(cookies)
url="https://i.2haohr.com/api/person_ucenter_auth/wechat_login/login/"
data={"key":"dcfd4bc3acf246faa05d4b8c581c9ddc","uid":"89d64e71342e4e809a7b95da6631c0e9"}
r=requests.post(url,data)
accesstoken=r.json()["data"]["accesstoken"]
print(accesstoken)


value=parse.urlencode({"token":accesstoken,"status":0})

driver.add_cookie({"name":"sessionid","value":accesstoken})
# cookie1={u'employee-accesstoken-pd': u'token=mv7se6d50lgigvf97q0j6j7osdouxn6z&status=0',
#       u'sessionid': u'7g99ts9orhn5m6purbegewtrog2i7172',
#       u'employee-accesstoken-pd':'%7B%22token%22%3A%227g99ts9orhn5m6purbegewtrog2i7172%22%2C%22status%22%3A0%7D'}
# c1={u'employee-accesstoken-pd':u'%7B%22token%22%3A%2261ylkhvorx9jkk0lz2diqdlop1hybecg%22%2C%22status%22%3A0%7D'}
# driver.add_cookie(c1)






driver.refresh()#刷新
cookies=driver.get_cookies()
print(cookies)

