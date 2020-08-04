from frameworkutils.base_page import BasePage


class UserCenter(BasePage):
    #基本信息编辑按钮
    edit_info_button="xpath=>//span[text()='编辑']"




    #点击基本信息编辑按钮
    def click_edit_info_button(self):
        self.click(self.edit_info_button)

