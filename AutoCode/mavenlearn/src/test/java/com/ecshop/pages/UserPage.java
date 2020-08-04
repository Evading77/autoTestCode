package com.ecshop.pages;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class UserPage {
	List<WebElement> reg_input_list=new ArrayList();
	private WebDriver driver;
	@FindBy(name="username")
	private WebElement input_username;
	@FindBy(name="password")
	private WebElement input_password;
	@FindBy(name="submit")
	private WebElement btn_submit;
	@FindBy(css="div.boxCenterList > div >p")
	private WebElement login_result_text;
	
	@FindBy(id="username")
	private WebElement reg_input_username;
	@FindBy(id="email")
	private WebElement reg_input_email;
	@FindBy(id="password1")
	private WebElement reg_input_password;
	@FindBy(id="conform_password")
	private WebElement reg_input_conform_password;
	@FindBy(name="extend_field5")
	private WebElement reg_input_cellphone;
	@FindBy(name="Submit")
	private WebElement reg_input_submit;
	
	//运用页面工场构造自己
	public UserPage(WebDriver driver) {
		this.driver=driver;
		PageFactory.initElements(driver, this);
		reg_input_list.add(reg_input_username);
		reg_input_list.add(reg_input_email);
		reg_input_list.add(reg_input_password);
		reg_input_list.add(reg_input_conform_password);
		reg_input_list.add(reg_input_cellphone);
	}

	public void username_input(String u) {
		input_username.sendKeys(u);
	}
	public void password_input(String p) {
		input_password.sendKeys(p);
	}
	public void submit_btn() {
		btn_submit.click();
	}
	public void assert_result(String expected) {
		String actual=login_result_text.getText();
		assertEquals(actual, expected);
	}
	public void assert_alert_text(String expected) {
		Alert alert =driver.switchTo().alert();
		String actual=alert.getText();
		alert.accept();
		assertTrue(actual.contains(expected));
	}
	public void reg_input_info(int index,String content) {
		reg_input_list.get(index-1).sendKeys(content);
	}
	public void reg_submit() {
		reg_input_submit.click();
	}
	public void assert_input_tip(int index,String expectedText) {
		String actual=reg_input_list.get(index-1).findElement(By.xpath("../span")).getText();
		assertTrue(actual.contains(expectedText));
	}
}
