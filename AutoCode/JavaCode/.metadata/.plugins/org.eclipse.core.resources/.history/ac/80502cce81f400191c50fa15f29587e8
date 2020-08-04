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
		logger.info("获取系统属性test.browser，值为"+browser);
		Config config=new Config("config.properties");
		String driverFile=config.getConfig("driver");
		logger.info("获取配置文件中driver所在路径，值为"+driverFile);
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
			throw new RuntimeException("未支持的浏览器");
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
			throw new RuntimeException("未支持的浏览器");
		}
		driver=new RemoteWebDriver(service.getUrl(),caps);
		return driver;
	}
	public static void stopService() {
		service.stop();
	}
}

