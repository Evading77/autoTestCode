package com.ecshop.utils;

import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;

public class RetryAnalysis implements IRetryAnalyzer {
	private static final int Max=1;
	private int count;
	@Override
	public boolean retry(ITestResult result) {
		if(count<=Max) {
			count++;
			return true;
		}
		return false;
	}

}
