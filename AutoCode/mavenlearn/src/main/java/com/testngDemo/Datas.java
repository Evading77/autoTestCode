package com.testngDemo;

import org.testng.annotations.DataProvider;

public class Datas {
	@DataProvider(name="auth")
	public static Object[][] getData(){
		return new Object[][] {
			{"ding","123"},
			{"eing","456"},
			{"ong","579"}
		};
	}
}
