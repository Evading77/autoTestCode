from frameworkutils.base_page import BasePage


class Desk(BasePage):
    approval_menu="xpath=>//div[@id='top-bar-menus']/a/span[text()='审批']"
    approval_draggable="xpath=>//div[@draggable='true']/../span[text()='审批']"
    more_menu="xpath=>//span[text()='更多']"
    new_approval_button = "xpath=>//span[text()='+新建审批表单']"
    anpaimainshi="xpath=>//span[text()='安排面试']"
    #招聘
    recruitment_menu="xpath=>//div[@id='top-bar-menus']/a/span[text()='招聘']"
    #用户中心菜单
    user_center="xpath=>//img[@tabindex='0']"
    #个人中心
    user_center_title="xpath=>//h1"

    def click_approval_menu(self):
        self.click(self.approval_menu)

    def click_approval_draggable(self):
        self.click(self.approval_draggable)

    def click_more_menu(self):
        self.click(self.more_menu)

    def click_recruitment_menu(self):
        self.click(self.recruitment_menu)

    def click_user_center(self):
        self.click(self.user_center)