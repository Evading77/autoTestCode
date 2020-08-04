package com.ecshop.data;

import org.testng.annotations.DataProvider;

import com.ecshop.utils.ReadExcel;

public class TestDataFactory {
	@DataProvider(name="loginData")
	public Object[][] LoginData(){
//		return new Object[][] {
//			{"root","123456","��¼�ɹ�"},
//			{"root","56674","�û������������"},
//			{"root123","123456","�û������������"},
//			{"root","","��¼���벻��Ϊ��"},
//			{"","123456","�û�������Ϊ��"}
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
