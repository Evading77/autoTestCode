package com.utils;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeMethod;

public class BaseTest {
	public WebDriver driver;
	@AfterSuite
	public void closeService() {
		DriverUtils.stopService();
	}
	@BeforeMethod
	public void initDriver() {
		Config config=new Config("config.properties");
		System.setProperty("test.browser", config.getConfig("test.browser"));
		driver=DriverUtils.getDriver();
	}
	@AfterMethod
	public void quitDriver() {
		driver.quit();
	}
}
