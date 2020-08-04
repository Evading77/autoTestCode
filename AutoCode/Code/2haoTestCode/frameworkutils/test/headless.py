from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://map.baidu.com/")
driver.save_screenshot("baidu-map.png")

import selenium
import selenium
