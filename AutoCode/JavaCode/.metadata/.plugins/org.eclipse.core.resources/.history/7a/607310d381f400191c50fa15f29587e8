package com.ecshop.utils;

import java.io.File;
import java.net.URL;
import java.util.List;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.Capabilities;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.RemoteWebDriver;

public class WrappedRemoteWebDriver extends RemoteWebDriver {
	//包装的RemotewebDriver，继承了RemoteWebDriver，重写了findElement和findElements方法，实现元素查找时的日志记录
	private Logger logger=LogManager.getLogger();
	public WrappedRemoteWebDriver(URL remoteAddress,Capabilities capabilities) {
		super(remoteAddress,capabilities);
	}
	@Override
	protected WebElement findElement(String by, String using) {
		WebElement element=null;
		try {
			element= super.findElement(by, using);
			logger.info("通过"+by+"方法查找"+using+"元素，已找到");
		}catch (Exception e) {
			logger.error("通过"+by+"方法查找"+using+"元素是发生异常，原因："+e.getMessage());
		}
		return element;
	}
	@Override
	protected List<WebElement> findElements(String by, String using) {
		List<WebElement> elements=null;
		try {
			elements= super.findElements(by, using);
			logger.info("通过"+by+"方法查找"+using+"元素，已找到"+elements.size()+"个");
		}catch (Exception e) {
			logger.error("通过"+by+"方法查找"+using+"元素是发生异常，原因："+e.getMessage());
		}
		return elements;
	}
	
	public void takeScreenShot(String filename) {
		File screenShot=((TakesScreenshot)this).getScreenshotAs(OutputType.FILE);
		File directory=new File("ScreenShots");
		if(!directory.exists()||!directory.isDirectory()) {
			logger.info("ScreenShots目录不存在，创建该目录");
			directory.mkdir();
		}
		File file=new File(directory,filename);
		screenShot.renameTo(file);
		logger.info("截屏保存成功，保存在："+file.getAbsolutePath());
	}
}
