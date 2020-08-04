package com.ecshop.data;

import org.testng.annotations.DataProvider;

import com.ecshop.utils.ReadExcel;

public class TestDataFactory {
	@DataProvider(name="loginData")
	public Object[][] LoginData(){
//		return new Object[][] {
//			{"root","123456","登录成功"},
//			{"root","56674","用户名或密码错误"},
//			{"root123","123456","用户名或密码错误"},
//			{"root","","登录密码不能为空"},
//			{"","123456","用户名不能为空"}
//		};
		return ReadExcel.getDataFromExcel("LoginTestData.xlsx", "Sheet1");
	}
	@DataProvider(name="registerData")
	public Object[][] RegisterData(){
		return ReadExcel.getDataFromExcel("RegisterTestData.xlsx", "Sheet1");
	}
	@DataProvider(name="registerSuccessData")
	public Object[][] RegisterSuccessData(){
		return ReadExcel.getDataFromExcel("RegisterTestData.xlsx", "Sheet2");
	}
}
