package com.testngDemo;

import org.testng.ITestResult;
import org.testng.TestListenerAdapter;

public class ListenerTest extends TestListenerAdapter {
	@Override
	public void onTestFailure(ITestResult tr) {
		super.onTestFailure(tr);
		System.out.println("F");
	}
	@Override
	public void onTestSuccess(ITestResult tr) {
		super.onTestSuccess(tr);
		System.out.println("S");
	}
}
