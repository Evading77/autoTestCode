import time
import unittest

from frameworkutils.browserbase import BrowerBase
from pageobjects.functions.desk import Desk
from pageobjects.functions.loginPage import Login

from pageobjects.functions.recruitment import Recruitment


class Test_Recruitment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowerBase(cls)
        cls.driver = browser.open_browser(cls)
        # browser.login_success()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("结束")

#手机登录系统
    def test_1login_success(self):
        loginpage = Login(self.driver)
        loginpage.click_cell_login()
        loginpage.type_cellphone()
        loginpage.click_next()
        loginpage.type_pwd()
        loginpage.click_login_button()
        if loginpage.is_exist_element(loginpage.close_news):
            loginpage.click_close_news()
        self.assertIsNotNone(loginpage.login_success_ico)
        time.sleep(2)
#进去招聘页面
    def test_2recruitment(self):
        deskpage = Desk(self.driver)
        time.sleep(2)
        deskpage.click_recruitment_menu()
        time.sleep(2)
        self.assertIsNotNone(deskpage.anpaimainshi)

#新建招聘职位
    @unittest.skipIf(True,u"为True的时候跳过")
    def test_3new_job_position(self):
        jobpositionpage=Recruitment(self.driver)
        jobpositionpage.click_job_position_menu()
        jobpositionpage.click_add_position_button()
        jobpositionpage.input_job_name()
        time.sleep(2)
        jobpositionpage.click_job_save_button()

#新建候选人
    def test_3candidatelist(self):
        jobpositionpage = Recruitment(self.driver)
        jobpositionpage.click_candidate_list_menu()
        jobpositionpage.choose_add_candidate()
        se=jobpositionpage.job_selection
        jobpositionpage.choose_job()
        jobpositionpage.input_candidate_name()
        jobpositionpage.input_cellphone()
        jobpositionpage.click_save()
        self.driver.execute_script()




