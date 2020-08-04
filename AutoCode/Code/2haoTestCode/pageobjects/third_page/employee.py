from frameworkutils.base_page import BasePage


class Employee(BasePage):
    #人事一级菜单
    employee_menu="xpath=>//div[@id='top-bar-menus']/a/span[text()='人事']"
    #员工管理
    #员工花名册菜单
    employee_roster="xpath=>//a[contains(@href,'roster')]"
    #添加员工
    add_employee="xpath=>//span[text()='添加员工']"
    #添加待入职
    add_candidate="xpath=>//span[text()='待入职']"
    #扫码入职
    add_sweepCode = "xpath=>//span[text()='扫码入职']"
    #返回按钮
    back_button="xpath=>//span[text()='返回']"
    #导入花名册
    import_roster = "xpath=>//span[text()='导入花名册']"
    #高级搜索
    advanced_search = "xpath=>//span[text()='高级搜索']"
    #更多功能
    more_functions = "xpath=>//button[@class='ivu-btn']/span/i"

    #员工档案库
    employee_archive = "xpath=>//a[contains(@href,'archive')]"
    #员工档案概况
    survey="xpath=>//a[text()='员工档案概况']"
    #教育经历
    education = "xpath=>//a[text()='教育经历']"
    #工作经历
    work_experience = "xpath=>//a[text()='工作经历']"
    #证书/证件
    professional = "xpath=>//a[text()='证书/证件']"
    #紧急联系人
    contact = "xpath=>//a[text()='紧急联系人']"
    #家庭成员
    family = "xpath=>//a[text()='家庭成员']"
    #职称
    title = "xpath=>//a[text()='职称']"
    #工作技能
    work_skill = "xpath=>//a[text()='工作技能']"
    #语言能力
    language = "xpath=>//a[text()='语言能力']"

    #统计分析
    employee_statistics = "xpath=>//a[contains(@href,'statistics')]"
    # 员工概况
    overview = "xpath=>//a[text()='员工概况']"
    # 趋势分析
    trend_analysis = "xpath=>//a[text()='趋势分析']"
    # 年度分析
    annual_analysis = "xpath=>//a[text()='年度分析']"
    # 员工分布
    employee_distribution = "xpath=>//a[text()='员工分布']"

    #人事报表
    employee_personnel_report = "xpath=>//a[contains(@href,'personnel-report')]"
    # 添加报表
    add_template = "xpath=>//span[text()='添加报表']"
    #返回
    back_add_template="xpath=>//a[text()='返回']"
    # 编辑分组
    edit_group = "xpath=>//span[text()='编辑分组']"

    #万能人事表格
    employee_all_purpose_form = "xpath=>//a[contains(@href,'all-purpose-form')]"
    #人事动态
    employee_dynamic = "xpath=>//a[contains(@href,'dynamic')]"


    #员工关系
    #入职管理
    employee_entry = "xpath=>//a[contains(@href,'entry')]"
    # 发送入职登记表
    send_ruzhidengji = "xpath=>//span[text()='发送入职登记表']"
    # 确认入职
    certain_entry = "xpath=>//span[text()='发送入职登记表']"
    #批量操作
    piliangcz = "xpath=>//button[@class='ivu-btn']/span/i"

    #转正管理
    employee_probation = "xpath=>//a[contains(@href,'probation')]"
    # 批量调整转正日期
    piliangtz = "xpath=>//span[text()='批量调整转正日期']"

    #离职管理
    employee_departure = "xpath=>//a[contains(@href,'departure')]"
    #办理离职
    banlilz="xpath=>//button[@class='ivu-btn ivu-btn-primary']"
    # 批量办理离职
    pl_banlilz = "xpath=>//button[@class='ivu-btn']"

    #人事异动
    employee_unusual_action = "xpath=>//a[contains(@href,'unusual-action')]"
    #批量转全职
    pl_zhuanqz="xpath=>//div[@class='ivu-col']/button[@class='ivu-btn ivu-btn-primary']"

    #员工关怀
    employee_care = "xpath=>//a[contains(@href,'care')]"
    #员工生日
    birthday="xpath=>//h3[text()='员工生日']"
    # 员工入职周年
    anniversary = "xpath=>//h3[text()='员工入职周年']"
    # 短信通知
    batch_sms = "xpath=>//h3[text()='短信通知']"

    #合同管理
    employee_contract = "xpath=>//a[contains(@href,'contract')]"
    # 已签订合同
    signed = "xpath=>//a[text()='已签订合同']"
    # 未签订合同
    not_signed = "xpath=>//a[text()='未签订合同']"
    # 合同签订记录
    record = "xpath=>//a[text()='合同签订记录']"
    # 合同概况
    hetonggk = "xpath=>//a[text()='合同概况']"

    #沟通记录
    employee_talk = "xpath=>//a[contains(@href,'talk')]"
    #添加沟通记录
    add_record = "xpath=>//span[text()='添加沟通记录']"
    #设置沟通类型
    talk_setting = "xpath=>//span[text()='设置沟通类型']"

    #任职记录
    employee_officeholding = "xpath=>//a[contains(@href,'officeholding')]"
    #新增
    add_officeholding = "xpath=>//span[text()='新增']"

    #培训经历
    employee_training = "xpath=>//a[contains(@href,'training')]"
    # 新增
    add_training = "xpath=>//span[text()='新增']"

    #奖惩记录
    employee_award="xpath=>//a[contains(@href,'award')]"
    # 新增
    add_award = "xpath=>//span[text()='新增']"



