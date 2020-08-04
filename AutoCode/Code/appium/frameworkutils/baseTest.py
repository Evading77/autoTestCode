import configparser
import os
import time

from appium import webdriver

from frameworkutils.logger import Logger

logger = Logger(logger="BaseTest").getlog()
class BaseTest(object):
    def __init__(self, driver):
        self.driver = driver

    #获取driver
    def getDriver(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path, encoding='utf-8')  # 如果代码有中文注释，用这个，不然报解码错误

        platformName = config.get("desiredCapabilites", "platformName")
        platformVersion = config.get("desiredCapabilites", "platformVersion")
        deviceName = config.get("desiredCapabilites", "deviceName")
        appPackage = config.get("desiredCapabilites", "appPackage")
        appActivity = config.get("desiredCapabilites", "appActivity")
        automationName = config.get("desiredCapabilites", "automationName")
        noReset = config.get("desiredCapabilites", "noReset")
        chromeOptions = config.get("desiredCapabilites", "chromeOptions")
        androidProcess = config.get("desiredCapabilites", "androidProcess")
        unicodeKeyboard=config.get("desiredCapabilites","unicodeKeyboard")
        resetKeyboard=config.get("desiredCapabilites","resetKeyboard")
        desired_caps = {
            'platformName': platformName,
            'platformVersion': platformVersion,
            'deviceName': deviceName,
            'appPackage': appPackage,
            'appActivity': appActivity,
            'automationName': automationName,
            'noReset': noReset,
            'chromeOptions': chromeOptions,
            'androidProcess': androidProcess,
            'unicodeKeyboard':unicodeKeyboard,
            'resetKeyboard':resetKeyboard
        }
        driver = webdriver.Remote(r'http://localhost:4723/wd/hub', desired_caps)
        return driver






