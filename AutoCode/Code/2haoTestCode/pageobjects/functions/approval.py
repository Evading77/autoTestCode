from frameworkutils.base_page import BasePage


class Approval(BasePage):
    new_approval_button="xpath=>//span[text()='+新建审批表单']"
    new_luyong="xpath=>//span[text()='录用']"
    # 发起审批
    faqishenpi="xpath=>//div[@class='ivu-poptip-rel']"
    # 前往员工端
    yuangongduan="xpath=>//span[text()='前往员工服务平台']"
    #微信扫码登录员工服务平台
    weixinsaoma="xpath=>//img[contains(@src,'weixin.qq')]"

    def click_new_approval_button(self):
        self.click(self.new_approval_button)

    def click_faqishenpi(self):
        self.click(self.faqishenpi)

    def click_yuangongduan(self):
        self.click(self.yuangongduan)