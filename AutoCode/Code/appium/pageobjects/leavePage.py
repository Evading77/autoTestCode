import time

from selenium.webdriver.common.by import By

from frameworkutils.functionBase import FunctionBase


class LeavePage(FunctionBase):
#元素定位
    #请假审批
    leave_approval=(By.XPATH,"//*[@text='请假']")
    #申请人
    applicant_option=(By.XPATH,"//*[@text='芸芸众生']")
    #选择联系人输入框
    select_applicant_input=(By.XPATH,"//*[@text='请输入员工姓名/手机号进行搜索']")
    #申请人岗位
    applicant_job=(By.XPATH,"//*[@text='人事专员']")
    #确认按钮contains
    confirm_contains_button=(By.XPATH,"//*[contains(@text,'确定')]")
    #确认按钮
    confirm_button=(By.XPATH,"//*[@text='确定']")
    #请假类型
    leave_type=(By.XPATH,"//*[@text='请假类型']")
    #开始时间
    start_time=(By.XPATH,"//*[@text='开始时间']")
    #结束时间
    end_time=(By.XPATH,"//*[@text='结束时间']")
    #时长
    time_length=(By.XPATH,"//*[contains(@text,'时长')]/../../android.view.View[2]")
    #时长控件
    time_length_ele=(By.XPATH,"//*[contains(@text,'时长')]")
    #数字键盘"删除"
    number_keyboard_delete=(By.ID,"com.tencent.mm:id/tenpay_keyboard_d")
    # 数字键盘"0"
    number_keyboard_0=(By.ID,"com.tencent.mm:id/tenpay_keyboard_0")
    # 数字键盘"."
    number_keyboard_x = (By.ID, "com.tencent.mm:id/tenpay_keyboard_x")
    # 数字键盘"1"
    number_keyboard_1 = (By.ID, "com.tencent.mm:id/tenpay_keyboard_1")
    #发起时的统计
    statistics_initiate=(By.XPATH,"//*[contains(@text,'本月累计请假')]")
    #发起请假时是否有统计标记
    flag=False
    #请假事由
    # leave_reason=(By.XPATH,"//*[@text='请假事由']/../android.view.View[2]")
    #上传文件
    # upload_button=(By.XPATH,"//*[@text='上传文件')]/../android.view.View[2]/*")
    #所在部门

    #添加审批人按钮(发起没有统计信息)
    add_approver_button_nostatistics=(By.XPATH,"//*[@text='审批人']/../android.view.View[17]")
    #添加审批人按钮(发起有统计信息)
    add_approver_button_statistics=(By.XPATH,"//*[@text='审批人']/../android.view.View[18]")
    #审批人岗位
    approver_job=(By.XPATH,"//*[@text='产品经理']")
    #添加抄送人(发起没有统计信息)
    add_copy_button_nostatistics=(By.XPATH,"//*[@text='抄送人']/../android.view.View[21]")
    #添加抄送人(发起有统计信息)
    add_copy_button_statistics=(By.XPATH,"//*[@text='抄送人']/../android.view.View[22]")
    #抄送人岗位
    copy_job=(By.XPATH,"//*[@text='岗位八']")
    #手写签名按钮
    sign_button=(By.XPATH,"//*[@text='点击手写签名']")
    #提交
    submit_button=(By.XPATH,"//*[@text='提交 ']")
    #修改时长后弹窗确认提交
    submit_time_length=(By.ID,"com.tencent.mm:id/b29")

#元素方法
    #点击请假审批
    def click_leave_approval(self):
        self.click(self.leave_approval)

    #切换申请人
    def switch_applicant(self):
        self.click(self.applicant_option)
        self.click(self.select_applicant_input)
        self.type(self.select_applicant_input,"于涛")
        self.click(self.applicant_job)
        self.click(self.confirm_contains_button)

    #选择请假类型
    def select_leave_type(self):
        self.click(self.leave_type)
        self.click(self.confirm_button)

    #选择请假时间
    def select_leave_time(self):
        self.click(self.start_time)
        self.click(self.confirm_button)
        self.click(self.end_time)
        self.click(self.confirm_button)
        self.flag=self.isExist(self.statistics_initiate)

    #修改时长
    def modify_time_length(self):
        self.click(self.time_length)
        # self.type(self.time_length, ".1")
        # self.click(self.number_keyboard_delete)
        # self.click(self.number_keyboard_0)
        self.click(self.number_keyboard_x)
        self.click(self.number_keyboard_1)
        self.click(self.time_length_ele)

    #添加审批人
    def add_approver(self):
        if self.flag:
            self.click(self.add_approver_button_statistics)
        else:
            self.click(self.add_approver_button_nostatistics)
        self.click(self.select_applicant_input)
        self.type(self.select_applicant_input, "芸芸众生")
        self.click(self.approver_job)
        self.click(self.confirm_contains_button)

    #添加抄送人
    def add_copy(self):
        if self.flag:
            self.click(self.add_copy_button_statistics)
        else:
            self.click(self.add_copy_button_nostatistics)
        self.click(self.select_applicant_input)
        self.type(self.select_applicant_input, "丁丁")
        self.click(self.copy_job)
        self.click(self.confirm_contains_button)

    #手写签名
    def sign_operation(self):
        self.click(self.sign_button)
        time.sleep(1)
        functionbase = FunctionBase(self.driver)
        functionbase.swipeDown()
        time.sleep(2)
        self.click(self.confirm_button)
        time.sleep(1)
        functionbase.swipeUp(0.25)

    #提交
    def click_submit_button(self):
        self.click(self.submit_button)

    # 修改时长后弹窗确认提交
    def click_submit_time_length(self):
        self.click(self.submit_time_length)












