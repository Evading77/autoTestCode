import os
import re
import time

import openpyxl


class ThirdPageCheck(object):
    #跳转三级菜单公共测试方法
    def third_pages_check(self):
        # 打开excel文件,获取工作簿对象
        filePath=os.path.dirname(os.path.abspath('.')) + '/config/employee.xlsx'
        wb = openpyxl.load_workbook(filePath)
        # 从表单中获取单元格的内容
        ws = wb.active  # 当前活跃的表单
        for row in ws.iter_rows(min_row=2, min_col=2, max_row=ws.max_row, max_col=2):  # 打印1-2行，1-2列中的内容
            for cell in row:
                xpath_value = str(cell.value)
                if "assert:" in cell.value:
                    assertXpath = 'xpath=>' + re.split(":", cell.value)[1]
                    self.assert_ele_is_exist(assertXpath)
                else:
                    self.driver.find_element_by_xpath(xpath_value).click()
                    time.sleep(1)