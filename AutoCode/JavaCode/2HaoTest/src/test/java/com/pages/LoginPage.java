package com.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
	//�ֻ��ŵ�¼
	@FindBy(xpath="//*/div/span[text()='�ֻ��ŵ�¼']")
	private WebElement cell_login;
	//�ֻ��������
	@FindBy(xpath="//*/input[@placeholder='�������ֻ���']")
	private WebElement cellphone_input;
	//��һ��
	@FindBy(xpath="//*/button[@size='large']")
	private WebElement next_step;
	//����������
	@FindBy(xpath="//*/input[@placeholder='����������']")
	private WebElement pwd_input;
	//���ϵ�¼
	@FindBy(xpath="//*/span[text()='���ϵ�¼']")
	private WebElement login_button;
	//�ر���Ϣ����
	@FindBy(xpath="//div[@class='popupWrap_egN7r']/../../div[1]/*")
	private WebElement close_news;
	//��¼�ɹ�����û�ͼ��
	@FindBy(xpath="//img[contains(@src,'brand')]")
	private WebElement login_success_ico;
	
	//ʹ��ҳ�湤�������Լ�
		public LoginPage(WebDriver driver) {
			PageFactory.initElements(driver, this);
		}
	//����ֻ���¼
	public void click_cell_login() {
		cell_login.click();
	}
	//�����ֻ���
	public void type_cellphone() {
		cell_login.sendKeys("13076998012");
	}
	//�����һ��
	public void click_next() {
		next_step.click();
	}
	//��������
	public void type_pwd() {
		pwd_input.sendKeys("dfy123");
	}
	//����ύ
	public void click_login_button() {
		login_button.click();
	}
	//�رյ���
	public void click_close_news() {
		close_news.click();
	}
	
}