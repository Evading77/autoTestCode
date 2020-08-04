package com.tests;


import org.testng.annotations.Test;

import com.pages.LoginPage;
import com.utils.BaseTest;

public class LoginTest extends BaseTest {
	@Test
	public void testLogin() {
		driver.get("https://2haohr.com");
		LoginPage loginp=new LoginPage(driver);
		loginp.click_cell_login();
		loginp.type_cellphone();
		loginp.click_next();
		loginp.type_pwd();
		loginp.click_login_button();
		
		
		
	}
}
