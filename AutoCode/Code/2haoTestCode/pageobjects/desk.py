from frameworkutils.base_page import BasePage


class Desk(BasePage):
    approval_menu="xpath=>//div[@id='top-bar-menus']/a/span[text()='审批']"
    approval_draggable="xpath=>//div[@draggable='true']/../span[text()='审批']"
    more_menu="xpath=>//span[text()='更多']"
    new_approval_button = "xpath=>//span[text()='+新建审批表单']"



    def click_approval_menu(self):
        self.click(self.approval_menu)

    def click_approval_draggable(self):
        self.click(self.approval_draggable)

    def click_more_menu(self):
        self.click(self.more_menu)