import os
import time

from frameworkutils.logger import Logger

logger = Logger(logger="FunctionBase").getlog()
class FunctionBase(object):
    def __init__(self, driver):
        self.driver = driver

    # 进入2号审批小程序
    def intoProgram(self):
        self.driver.implicitly_wait(20)
        time.sleep(7)
        # 向下滑动
        self.swipeDown()
        # 点击2号审批小程序
        self.driver.find_element_by_id("com.tencent.mm:id/zs").click()
        time.sleep(6)

# 通用操作
    # 向下滑动
    def swipeDown(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向上滑动
    def swipeUp(self, yn, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * yn  # 终点y坐标
        # y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动
    def swipe_left(self, t=500, n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动
    def swipe_right(self, t=500, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # 保存截图
    def get_screenshot(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_screenshot()

    # 点击元素
    def click(self, selector):
        ele = self.driver.find_element(*selector)
        try:
            ele.click()
            logger.info("The element \' %s \' was clicked." % ele.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
            self.get_screenshot()

    # 输入内容
    # def type(self, selector, text):
    #
    #     ele = self.driver.find_element(*selector)
    #     ele.click()
    #     # ele.clear()
    #     try:
    #         ele.send_keys(text)
    #         logger.info("Had type \' %s \' in inputBox" % text)
    #     except NameError as e:
    #         logger.error("Failed to type in input box with %s" % e)
    #         self.get_screenshot()
    def type(self, selector, text):
        ele = self.driver.find_element(*selector)
        time.sleep(1)
        ele.send_keys(text)
        # try:
        #     ele.send_keys(text)
        #     logger.info("Had type \' %s \' in inputBox" % text)
        # except NameError as e:
        #     logger.error("Failed to type in input box with %s" % e)
        #     self.get_screenshot()

    #判断元素是否存在
    def isExist(self,selector):
        flag = True
        try:
            self.driver.find_element(*selector)
            return flag
        except:
            flag = False
            return flag