package com.ecshop.tests;

import org.testng.annotations.Test;

import com.ecshop.data.TestDataFactory;
import com.ecshop.pages.IndexPage;
import com.ecshop.pages.UserPage;
import com.ecshop.utils.BaseTest;

public class RegisterTest extends BaseTest {
	@Test(dataProvider="registerData",dataProviderClass=TestDataFactory.class)
	public void testRegister(String contents,String expectedTexts ) {
		String[] con_arr=contents.split(",");
		String[] exp_arr=expectedTexts.split(",");
		driver.get("http://localhost/ecshop/index.php");
		IndexPage indexp=new IndexPage(driver);
		indexp.register_click();
		UserPage userp=new UserPage(driver);
		for(int i=1;i<=con_arr.length;i++) {
			userp.reg_input_info(i, con_arr[i-1]);
		}
		for(int i=1;i<exp_arr.length;i++) {
			userp.assert_input_tip(i, exp_arr[i-1]);
		}
	}
	@Test(dataProvider="registerSuccessData",dataProviderClass=TestDataFactory.class)
	public void testRegisterSuccess(String username,String email,String password,String con_password,String cellphone,String expectedText) {
		driver.get("http://localhost/ecshop/index.php");
		IndexPage indexp=new IndexPage(driver);
		indexp.register_click();
		UserPage userp=new UserPage(driver);
		userp.reg_input_info(1, username);
		userp.reg_input_info(2, email);
		userp.reg_input_info(3, password);
		userp.reg_input_info(4, con_password);
		userp.reg_input_info(5, cellphone);
		userp.reg_submit();
		userp.assert_result(expectedText);
	}
}
