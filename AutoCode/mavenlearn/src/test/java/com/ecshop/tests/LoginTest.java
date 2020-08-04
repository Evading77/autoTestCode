package com.ecshop.tests;

import org.testng.annotations.Test;

import com.ecshop.data.TestDataFactory;
import com.ecshop.pages.IndexPage;
import com.ecshop.pages.UserPage;
import com.ecshop.utils.BaseTest;

public class LoginTest extends BaseTest {
	@Test(dataProviderClass=TestDataFactory.class,dataProvider="loginData")
	public void LoginTest(String u,String p,String expectedText) {
		//		打开首页
		driver.get("http://localhost/ecshop/index.php");
		//		点击登录链接
		IndexPage indexp=new IndexPage(driver);
		indexp.login_click();
		//		填写用户名、密码
		UserPage userp=new UserPage(driver);
		userp.username_input(u);
		userp.password_input(p);
		//		点击立即登录按钮
		userp.submit_btn();
		//		判断是否登录成功
		if(u.equals("")||p.equals("")) {
			userp.assert_alert_text(expectedText);
		}else {
			userp.assert_result(expectedText);
		}
	}
}
