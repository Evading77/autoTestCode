import configparser
import os
import time

from appium import webdriver


config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
# config.read(file_path)
config.read(file_path,encoding='UTF-8')#如果代码有中文注释，用这个，不然报解码错误
platformName=config.get("desiredCapabilites","platformName")
platformVersion=config.get("desiredCapabilites","platformVersion")
deviceName=config.get("desiredCapabilites","deviceName")
appPackage=config.get("desiredCapabilites","appPackage")
appActivity=config.get("desiredCapabilites","appActivity")
automationName=config.get("desiredCapabilites","automationName")
noReset=config.get("desiredCapabilites","noReset")
chromeOptions=config.get("desiredCapabilites","chromeOptions")
androidProcess=config.get("desiredCapabilites","androidProcess")



desired_caps = {
                'platformName': platformName,
                #荣耀V10
                # 'platformVersion': '9',
                # 'deviceName': 'RKKDU18328001679',
                #测试机OPPO
                'platformVersion': platformVersion,
                'deviceName': deviceName,
                'appPackage': appPackage,
                'appActivity':appActivity,
                'automationName': automationName,
                'noReset': noReset,
                'chromeOptions':chromeOptions,
                'androidProcess':androidProcess
                }

# desired_caps = {
#                 # 'platformName': 'Android',
#                 'platformName': platformName,
#                 #荣耀V10
#                 # 'platformVersion': '9',
#                 # 'deviceName': 'RKKDU18328001679',
#                 #测试机OPPO
#                 'platformVersion': '5.1',
#                 'deviceName': 'YPN7NZ7T99999999',
#                 'appPackage': 'com.tencent.mm',
#                 'appActivity': '.ui.LauncherUI',
#                 'automationName': 'Uiautomator2',
#                 'noReset': True,
#                 # 'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
#                 'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand1'},
#                 'androidProcess':'com.tencent.mm:tools'
#                 # 'chromedriverExecutable':r'F:\Testing\testCode\HRUITest\tools\chromedriver.exe'
#                 }



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(20)
time.sleep(7)

def swipeDown(driver, t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.25  # 起始y坐标
    y2 = l['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
#
def swipeUp(driver,yn, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * yn  # 终点y坐标
    # y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

# 向下滑动
swipeDown(driver)
#点击2号审批小程序
driver.find_element_by_id("com.tencent.mm:id/a0x").click()
time.sleep(6)

# 请假审批
swipeUp(driver,0.6)
driver.find_element_by_xpath("//*[@text='请假']").click()
time.sleep(3)
#切换申请人
# driver.find_element_by_xpath("//*[@text='芸芸众生']").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").send_keys("于涛")
# driver.find_element_by_xpath("//*[@text='人事专员']").click()
# driver.find_element_by_xpath("//*[contains(@text,'确定')]").click()

driver.find_element_by_xpath("//*[@text='请假类型']").click()
driver.find_element_by_id("android:id/numberpicker_input").click()
driver.find_element_by_xpath("//*[@text='确定']").click()

driver.find_element_by_xpath("//*[@text='开始时间']").click()
driver.find_element_by_xpath("//*[@text='确定']").click()
driver.find_element_by_xpath("//*[@text='结束时间']").click()
driver.find_element_by_xpath("//*[@text='确定']").click()
#修改时长
driver.find_element_by_xpath("//*[contains(@text,'时长')]/../../android.view.View[2]").click()
# driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_0").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_x").click()
driver.find_element_by_id("com.tencent.mm:id/tenpay_keyboard_1").click()
driver.find_element_by_xpath("//*[contains(@text,'时长')]").click()
#输入请假事由
# driver.find_element_by_xpath("//*[@text='请假事由']/../android.view.View[2]").click()
# driver.find_element_by_xpath("//*[@text='请假事由']/../android.view.View[2]").send_keys("自动化测试请假")

#上传文件
# driver.find_element_by_xpath("//*[@text='上传文件')]/../android.view.View[2]/*").click()

swipeUp(driver,0.25)
time.sleep(1)
swipeUp(driver,0.25)
# #添加审批人
# driver.find_element_by_xpath("//*[@text='审批人']/../android.view.View[17]").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").send_keys("芸芸众生")
# driver.find_element_by_xpath("//*[@text='产品经理']").click()
# driver.find_element_by_xpath("//*[contains(@text,'确定')]").click()
# #添加抄送人
# driver.find_element_by_xpath("//*[@text='抄送人']/../android.view.View[21]").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").click()
# driver.find_element_by_xpath("//*[@text='请输入员工姓名/手机号进行搜索']").send_keys("丁丁")
# driver.find_element_by_xpath("//*[@text='岗位八']").click()
# driver.find_element_by_xpath("//*[contains(@text,'确定')]").click()
#手写签名
swipeUp(driver,0.25)
driver.find_element_by_xpath("//*[@text='点击手写签名']").click()
time.sleep(2)
swipeDown(driver)
driver.find_element_by_xpath("//*[@text='确定']").click()
time.sleep(2)
swipeUp(driver,0.25)
#提交
time.sleep(2)
driver.find_element_by_xpath("//*[@text='提交 ']").click()
time.sleep(2)
driver.find_element_by_id("com.tencent.mm:id/b29").click()





