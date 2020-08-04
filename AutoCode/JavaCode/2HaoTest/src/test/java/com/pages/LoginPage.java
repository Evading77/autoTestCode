package com.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
	//手机号登录
	@FindBy(xpath="//*/div/span[text()='手机号登录']")
	private WebElement cell_login;
	//手机号输入框
	@FindBy(xpath="//*/input[@placeholder='请输入手机号']")
	private WebElement cellphone_input;
	//下一步
	@FindBy(xpath="//*/button[@size='large']")
	private WebElement next_step;
	//请输入密码
	@FindBy(xpath="//*/input[@placeholder='请输入密码']")
	private WebElement pwd_input;
	//马上登录
	@FindBy(xpath="//*/span[text()='马上登录']")
	private WebElement login_button;
	//关闭消息弹窗
	@FindBy(xpath="//div[@class='popupWrap_egN7r']/../../div[1]/*")
	private WebElement close_news;
	//登录成功后的用户图标
	@FindBy(xpath="//img[contains(@src,'brand')]")
	private WebElement login_success_ico;
	
	//使用页面工场构造自己
		public LoginPage(WebDriver driver) {
			PageFactory.initElements(driver, this);
		}
	//点击手机登录
	public void click_cell_login() {
		cell_login.click();
	}
	//输入手机号
	public void type_cellphone() {
		cell_login.sendKeys("13076998012");
	}
	//点击下一步
	public void click_next() {
		next_step.click();
	}
	//输入密码
	public void type_pwd() {
		pwd_input.sendKeys("dfy123");
	}
	//点击提交
	public void click_login_button() {
		login_button.click();
	}
	//关闭弹窗
	public void click_close_news() {
		close_news.click();
	}
	
}
