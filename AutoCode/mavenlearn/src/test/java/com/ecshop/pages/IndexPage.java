package com.ecshop.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class IndexPage {
	@FindBy(linkText="���¼")
	private WebElement login_link;
	@FindBy(linkText="���ע��")
	private WebElement register_link;
	
	//ʹ��ҳ�湤�������Լ�
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