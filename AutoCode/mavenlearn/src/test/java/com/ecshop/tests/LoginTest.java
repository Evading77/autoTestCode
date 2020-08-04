package com.ecshop.tests;

import org.testng.annotations.Test;

import com.ecshop.data.TestDataFactory;
import com.ecshop.pages.IndexPage;
import com.ecshop.pages.UserPage;
import com.ecshop.utils.BaseTest;

public class LoginTest extends BaseTest {
	@Test(dataProviderClass=TestDataFactory.class,dataProvider="loginData")
	public void LoginTest(String u,String p,String expectedText) {
		//		����ҳ
		driver.get("http://localhost/ecshop/index.php");
		//		�����¼����
		IndexPage indexp=new IndexPage(driver);
		indexp.login_click();
		//		��д�û���������
		UserPage userp=new UserPage(driver);
		userp.username_input(u);
		userp.password_input(p);
		//		���������¼��ť
		userp.submit_btn();
		//		�ж��Ƿ��¼�ɹ�
		if(u.equals("")||p.equals("")) {
			userp.assert_alert_text(expectedText);
		}else {
			userp.assert_result(expectedText);
		}
	}
}
