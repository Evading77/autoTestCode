package com.ecshop.utils;

import java.io.File;
import java.io.IOException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.service.DriverService;

public class DriverUtils {
	private static DriverService service;
	private static String browser;
	private static final Logger logger=LogManager.getLogger();
	static{
		browser=System.getProperty("test.browser", "chrome");
		logger.info("��ȡϵͳ����test.browser��ֵΪ"+browser);
		Config config=new Config("config.properties");
		String driverFile=config.getConfig("driver");
		logger.info("��ȡ�����ļ���driver����·����ֵΪ"+driverFile);
		if("chrome".equalsIgnoreCase(browser)) {
			service=new ChromeDriverService.Builder()
					.usingDriverExecutable(new File(driverFile))
					.usingAnyFreePort()
					.build();	
		}else if("firefox".equalsIgnoreCase(browser)) {
			service=null;
		}else if("ie".equalsIgnoreCase(browser)) {
			service=null;
		}else {
			throw new RuntimeException("δ֧�ֵ������");
		}		
		try {
			service.start();
		} catch (IOException e) {
			e.printStackTrace();
		}	
	}
	
	public static WebDriver getDriver() {
		WebDriver driver=null;
		DesiredCapabilities caps=null;
		if("chrome".equalsIgnoreCase(browser)) {
			caps=DesiredCapabilities.chrome();
		}else if("firefox".equalsIgnoreCase(browser)) {
			caps=null;
		}else if("ie".equalsIgnoreCase(browser)) {
			caps=null;
		}else {
			throw new RuntimeException("δ֧�ֵ������");
		}
		driver=new RemoteWebDriver(service.getUrl(),caps);
		return driver;
	}
	public static void stopService() {
		service.stop();
	}
}

