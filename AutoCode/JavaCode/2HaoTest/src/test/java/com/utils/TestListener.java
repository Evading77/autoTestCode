package com.utils;

import java.lang.reflect.Field;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.testng.ITestResult;
import org.testng.TestListenerAdapter;

public class TestListener extends TestListenerAdapter {
	@Override
	public void onTestFailure(ITestResult tr) {
		try {
			Field field=tr.getTestClass().getRealClass().getField("driver");
			WrappedRemoteWebDriver driver=(WrappedRemoteWebDriver)field.get(tr.getInstance());
			String filename="";
			String className=tr.getTestClass().getName();
			String methodName=tr.getName();
			SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMddHHmmssSS");
			String time=sdf.format(new Date());
			filename=className+methodName+time+".png";
			driver.takeScreenShot(filename);
		} catch (NoSuchFieldException e) {
			e.printStackTrace();
		} catch (SecurityException e) {
			e.printStackTrace();
		}catch (IllegalArgumentException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			e.printStackTrace();
		}
		
	}
}
