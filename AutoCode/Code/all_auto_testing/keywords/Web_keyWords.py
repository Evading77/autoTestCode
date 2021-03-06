import os
import time
import traceback

from selenium import webdriver

from frameworkutils import logger
from frameworkutils.config import config
from frameworkutils.verify import Verify
from keywords.commenkeys import sysKey


class Web:
    """
    封装Web自动化函数
    """

    def __init__(self, writer):
        self.driver = None
        # 写入excel的对象
        self.writer = writer
        # 写入的行
        self.row = 0
        # 保存查找元素失败的异常
        self.e = None
        # 验证码识别
        self.verify = None

    def openbrowser(self, br="gc", ex=""):
        """
        打开浏览器
        :param br: gc=谷歌浏览器(默认)；ff=火狐浏览器；ie=ie浏览器
        :param ex: 对应driver的路径，默认在项目的lib目录
        :return: 打开成功失败
        """
        try:
            if br is None or br == "gc" or br == "":
                # 使用用户文件加载缓存和配置chrome的安装路径
                # 创建一个chrome的配置项对象
                option = webdriver.ChromeOptions()
                # 获取用户文件路径
                userfile = os.environ["USERPROFILE"]

                # 添加用户文件配置
                # 使用缓存，也使用了cookie
                option.add_argument("--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\user data"
                                    % userfile)
                # 配置chrome安装路径
                # option.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

                # 打开浏览器
                # driver就相当于打开的浏览器
                if ex == "":
                    ex = "./lib/conf/chromedriver.exe"

                self.driver = webdriver.Chrome(options=option, executable_path=ex)

            elif br == 'ff':
                if ex == "":
                    ex = "./lib/conf/geckodriver.exe"

                # 有cookie的，但是缓存不存在，所以加载还是比较慢
                # 使用cmd命令去创建一个用户文件
                # "C:\Program Files\Mozilla Firefox\firefox.exe" -p
                opt = webdriver.FirefoxOptions()
                opt.profile = r'%s\AppData\Roaming\Mozilla\Firefox\Profiles\mytest.mytest' % os.environ["USERPROFILE"]
                self.driver = webdriver.Firefox(executable_path=ex, firefox_options=opt)

            elif br == 'ie':
                if ex == "":
                    ex = "./lib/conf/IEDriverServer.exe"
                opt = webdriver.IeOptions()
                opt.profile = r'%s\Local\Microsoft\Windows\INetCache' % os.environ["USERPROFILE"]
                self.driver = webdriver.Ie(executable_path=ex, options=opt)

            # 添加隐式等待，凡是调find_element_xxx的地方，都会触发
            self.driver.implicitly_wait(10)
            self.__write_excel(True, "浏览器打开成功")
            # self.driver.find_element_by_partial_link_text()
            # self.driver.get_screenshot_as_png()

            try:
                self.verify = Verify(config.config['vusername'],
                                     config.config['vpassword'],config.config['soft_id'])
            except Exception as e:
                logger.warn("您暂不支持验证码识别")

            return True
        except Exception as e:
            logger.exception(e)
            self.__write_excel(False, traceback.format_exc())
            self.writer.save_close()
            # 退出，运行
            exit(-1)

    def geturl(self, url):
        """
        打开网站
        :param url: 输入网站
        :return: 打开成功/失败
        """
        if self.driver is None:
            self.__write_excel(False, "浏览器不存在")
            return False
        try:
            self.driver.get(url)
            self.__write_excel(True, "访问地址成功")
            return True
        except Exception as e:
            self.__write_excel(False, "访问地址失败")
            logger.exception(e)
            return False

    def click(self, locator):
        """
        通过定位器找到元素，并完成点击操作
        :param locator: 定位器
        :return: 点击成功/失败
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False
        try:
            ele.click()
            self.__write_excel(True, "点击成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def clickhref(self, locator):
        """
        通过定位器找到a标签元素，然后获取到href连接，进行跳转
        主要是处理IE点击失败的情况
        :param locator: 定位器
        :return: 点击成功/失败
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            href = ele.get_attribute('href')
            self.driver.get(href)
            self.__write_excel(True, "链接点击成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def jsclick(self, locator):
        """
        点击a标签，针对selenium点击不了的情况
        （点击a标签触发js事件的，JavaScript:void(0);）
        :param locator: 定位器
        :return: 点击成功/失败
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            self.driver.execute_script("$(arguments[0]).click()", ele)
            self.__write_excel(True, "点击成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def runjs(self, js):
        """
        点击a标签，针对selenium点击不了的情况
        （点击a标签触发js事件的，JavaScript:void(0);）
        :param locator: 定位器
        :return: 点击成功/失败
        """
        try:
            time.sleep(1)
            self.driver.execute_script(js)
            self.__write_excel(True, "点击成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def getimg(self,locator,filename=""):
        """
        获取元素截图
        :param locator: 定位器
        :param filename: 截图后保存的名字
        :return: 截图是否成功
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        if filename == '':
            filename = 'verify'

        try:
            filename = './lib/verify/' + filename + ".png"
            ele.screenshot(filename)
            self.__write_excel(True, "截图成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def getverify(self,codetype=''):
        """
        调用超级鹰识别验证码
        :param codetype: 验证码类型，默认1902
        :return: 识别是否成功
        """
        if codetype == "":
            codetype = 1902

        try:
            # 获取验证码
            v = self.verify.PostPic(int(codetype))
            if v is None:
                v = 'None'

            # 关联验证码
            sysKey.relations["verify"] = v
            self.__write_excel(True, "截图成功")
            return True
        except Exception as e:
            v = "None"
            # 关联验证码
            sysKey.relations["verify"] = v
            self.__write_excel(False, traceback.format_exc())
            return False


    def input(self, locator, text):
        """

        :param locator: 定位器
        :param text: 需要输入的文本
        :return: 输入是否成功
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            text = self.__get__relations(text)
            ele.send_keys(text)
            self.__write_excel(True, "输入成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def inputfile(self, locator, text):
        """

        :param locator: 定位器
        :param text: 需要输入的文本
        :return: 输入是否成功
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            text = sysKey.path + "/lib/verify/" + text
            ele.send_keys(text)
            self.__write_excel(True, "输入成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def sleep(self, t):
        """
        固定等待
        :param t: 时间，单位s
        :return: 返回成功失败
        """
        try:
            time.sleep(int(t))
            self.__write_excel(True, "等待")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def quit(self):
        """
        退出浏览器
        :return: 成功失败
        """
        try:
            self.driver.quit()
            self.__write_excel(True, "等待")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def gettext(self,locator,param="text"):
        """
        获取元素的文本，并保存为关联后参数名：param
        :param locator: 定位器
        :param param: 保存后的参数名
        :return: 获取成功失败
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            text = ele.text
            # 设置到关联字典
            sysKey.relations[param] = text
            self.__write_excel(True, "输入成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def assertcontains(self, expectv,actualv):
        """
        web断言关键字，断言实际结果包含预期结果
        :param expectv: 预期结果
        :param actualv: 实际结果
        :return: 是否包含
        """

        # 关联
        actualv = self.__get__relations(actualv)
        expectv = self.__get__relations(expectv)

        if actualv.__contains__(str(expectv)):
            self.__write_excel(True, actualv)
            return True
        else:
            self.__write_excel(False, actualv)
            return False

    def switchwindow(self,index=''):
        """
        窗口切换，切换到第index个窗口
        :param index: 窗口的下标
        :return: 切换是否成功
        """
        # 获取到所有窗口的handle列表
        if index == "" :
            index = 0

        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[int(index)])
            self.__write_excel(True, "切换窗口成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def intoiframe(self,locator):
        """
        进入locator指定的iframe
        :param locator: 定位iframe的定位器
        :return: 是否进入成功
        """
        ele = self.__find_ele(locator)
        if ele is None:
            self.__write_excel(False, self.e)
            return False

        try:
            # 进入iframe
            self.driver.switch_to.frame(ele)
            self.__write_excel(True, "输入成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False

    def outiframe(self):
        """
        退出iframe
        :return: 是否退出成功
        """
        try:
            # 退出到最外面的HTML
            self.driver.switch_to.default_content()
            self.__write_excel(True, "输入成功")
            return True
        except Exception as e:
            self.__write_excel(False, traceback.format_exc())
            return False


    def __get__relations(self, params):
        """
        使用关联结果
        :param params: 需要关联的参数
        :return: 关联后的字符串
        """
        if params is None:
            return None
        else:
            params = str(params)

        for key in sysKey.relations.keys():
            params = params.replace('{' + key + '}', str(sysKey.relations[key]))
        return params

    def __find_ele(self, locator):
        """
        通过定位器找到元素
        :param locator: xpath
        :return: 返回找到的元素
        """
        try:
            if locator.startswith("id="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_id(locator)
            elif locator.startswith("xpath="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_xpath(locator)
            elif locator.startswith("tagname="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_tag_name(locator)
            elif locator.startswith("name="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_name(locator)
            elif locator.startswith("linktext="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_link_text(locator)
            elif locator.startswith("css="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_css_selector(locator)
            elif locator.startswith("class="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_class_name(locator)
            elif locator.startswith("partial="):
                locator = locator[locator.find('=') + 1:]
                ele = self.driver.find_element_by_partial_link_text(locator)
            else:
                ele = self.driver.find_element_by_xpath(locator)
        except Exception as e:
            self.e = traceback.format_exc()
            return None

        return ele

    def __write_excel(self, status, msg):
        """
        写入关键字运行结果
        :param status: 运行的状态
        :param msg: 实际运行结果
        :return: 无
        """
        if status is True:
            self.writer.write(self.row, 7, "PASS", 3)
        else:
            self.writer.write(self.row, 7, "FAIL", 2)

        # 有时候实际结果过长，我们就只保存前1024个字符
        msg = str(msg)
        if len(msg) > 32767:
            msg = msg[0:32767]

        self.writer.write(self.row, 8, str(msg))