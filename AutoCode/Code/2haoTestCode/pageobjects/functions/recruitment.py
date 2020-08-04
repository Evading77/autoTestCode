import datetime
import random

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

from frameworkutils.base_page import BasePage


class Recruitment(BasePage):
    #招聘职位二级菜单
    job_position_menu="xpath=>//img[contains(@src,'BD%8D')]"
    #添加招聘职位按钮
    add_position_button="xpath=>//span[text()='添加招聘职位']"
    #添加招聘职位页面输入职位名称输入框
    job_name_input="xpath=>//div[@class='ivu-form-item ivu-form-item-required']/div/div/input"
    #职位名称带上时间
    job_name_string="AutoJob"+ datetime.datetime.now().strftime('%Y%m%d%H%M')
    #添加招聘职位页面仅保存按钮
    job_save_button="xpath=>//button[@class='ivu-btn']"
    #候选人二级菜单
    candidate_list_menu="xpath=>//img[contains(@src,'%BA%BA')]"
    #添加候选人
    candidate_add_button="xpath=>//button[@class='ivu-btn ivu-btn-primary']/span/i/.."
    #添加候选人方式：单个添加候选人
    candidate_add_single="xpath=>//li[text()='批量导入简历']/../li[1]"
    #添加候选人方式：批量导入简历
    candidate_add_resume="xpath=>//li[text()='批量导入简历']"
    #应聘职位
    # job_selection="xpath=>//label[text()='应聘职位']/../div/span/span/span/span/span"
    job_selection="xpath=>//select[1]"
    #下拉选项
    job_option="xpath=>//select/option[text()='老板职位']"
    #应聘职位搜索框
    job_search="xpath=>//input[@placeholder='请输入关键字']"
    #姓名输入框
    name_input="xpath=>//label[text()='姓名']/../div/div/input"
    # 新建候选人姓名带上时间
    candidate_name_string = "AutoName" + datetime.datetime.now().strftime('%Y%m%d%H%M')
    #输入手机号
    cellphone_input="xpath=>//label[text()='手机号']/../div/div/input"
    #手机号输入内容
    cellphone_string="135"+str(random.randint(10000000,99999999))
    #保存按钮
    save_button="xpath=>//button[@class='ivu-btn ivu-btn-cancel']/../button[2]"

#点击招聘职位二级菜单
    def click_job_position_menu(self):
        self.click(self.job_position_menu)
#点击添加招聘职位
    def click_add_position_button(self):
        self.click(self.add_position_button)
#输入招聘职位名称
    def input_job_name(self):
        self.type(self.job_name_input,self.job_name_string)
#点击添加招聘职位页面仅保存按钮
    def click_job_save_button(self):
        self.click(self.job_save_button)
#点击候选人列表二级菜单
    def click_candidate_list_menu(self):
        self.click(self.candidate_list_menu)
#点击添加候选人按钮，并选择添加候选人方式
    def choose_add_candidate(self):
        self.move_to_ele(self.candidate_add_button)
        self.sleep(1)
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.candidate_add_single))
        self.click(self.candidate_add_single)
#选择第一个招聘职位
    def choose_job(self):
        # self.type(self.job_selection, Keys.ENTER)
        # self.move_to_ele(self.job_search)
        # self.type(self.job_search,"AutoJob")
        # self.sleep(2)
        # self.type(self.job_search,Keys.ENTER)
        # 如是select标签就可以用下面方法
        s=Select(self.job_selection)
        s.select_by_index(1)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(WebElement(self.job_selection)))
        Select(WebElement(self.job_selection)).select_by_index(1)

#输入候选人姓名
    def input_candidate_name(self):
        self.type(self.name_input,self.candidate_name_string)
#输入手机号
    def input_cellphone(self):
        self.type(self.cellphone_input,self.cellphone_string)
#点击保存
    def click_save(self):
        self.click(self.save_button)