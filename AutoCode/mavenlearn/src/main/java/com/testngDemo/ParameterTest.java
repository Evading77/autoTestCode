package com.testngDemo;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParameterTest {
//	@DataProvider(name="auth")
//	public Object[][] getAuthData(){
//		return new Object[][] {
//			{"ding","123"},
//			{"eing","456"},
//			{"ong","579"}
//		};
//	}
	
	@Test(dataProvider="auth",dataProviderClass=Datas.class)
	public void test(String u,String p) {
		System.out.println("username:"+u+",password:"+p);
	}

}
