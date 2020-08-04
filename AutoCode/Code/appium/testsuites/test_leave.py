
import time
import unittest
from frameworkutils.baseTest import BaseTest
from frameworkutils.functionBase import FunctionBase
from pageobjects.leavePage import LeavePage


class TestLeaveApproval(unittest.TestCase,FunctionBase):
    @classmethod
    def setUpClass(cls):
        basetest=BaseTest(cls)
        cls.driver=basetest.getDriver(cls)


    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("结束")

    #进入审批小程序
    def test_1intoProgram(self):
        self.intoProgram()

    #发起请假审批
    def test_initiate_approval(self):
        functionbase = FunctionBase(self.driver)
        functionbase.swipeUp(0.6)
        leavepage=LeavePage(self.driver)
        #点击请假审批
        leavepage.click_leave_approval()
        time.sleep(3)
        #切换申请人
        leavepage.switch_applicant()
        # 选择请假类型
        leavepage.select_leave_type()
        # 选择请假时间
        leavepage.select_leave_time()
        # 修改时长
        leavepage.modify_time_length()
        # 添加审批人
        functionbase.swipeUp(0.25)
        time.sleep(1)
        functionbase.swipeUp(0.25)
        leavepage.add_approver()
        # 添加抄送人
        leavepage.add_copy()
        # 手写签名
        functionbase.swipeUp(0.25)
        leavepage.sign_operation()
        # 提交
        time.sleep(2)
        leavepage.click_submit_button()
        # 修改时长后弹窗确认提交
        time.sleep(2)
        leavepage.click_submit_time_length()







