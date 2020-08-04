package com.ecshop.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class IndexPage {
	@FindBy(linkText="请登录")
	private WebElement login_link;
	@FindBy(linkText="免费注册")
	private WebElement register_link;
	
	//使用页面工场构造自己
	public IndexPage(WebDriver driver) {
		PageFactory.initElements(driver, this);
	}
	
	public void login_click() {
		login_link.click();
	}
	public void register_click() {
		register_link.click();
	}
	
}