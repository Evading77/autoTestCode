package com.ecshop.utils;

import java.io.IOException;
import java.io.InputStream;

import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class ReadExcel {
	public static Object[][] getDataFromExcel(String excelFileName,String sheetName){
		Object[][] obj=null;
		//从类加载器路径中读取指定的文件，获得其输入流
		InputStream is=ReadExcel.class.getClassLoader().getResourceAsStream(excelFileName);
		Workbook wb=null;
		Sheet sheet=null;
		try {
			wb=new XSSFWorkbook(is);
			sheet=wb.getSheet(sheetName);
			int lastRowNum=sheet.getLastRowNum();
			//获取最后一个单元格的编号（列号），需要减1
			int lastCellNum=sheet.getRow(lastRowNum).getLastCellNum();
			obj=new Object[lastRowNum][lastCellNum];
			for(int i=1;i<=lastRowNum;i++) {
				for(int j=0;j<lastCellNum;j++) {
					String str=sheet.getRow(i).getCell(j).getStringCellValue();
					if(str.equalsIgnoreCase("<Empty>")) {
						obj[i-1][j]="";
					}else {
						obj[i-1][j]=str;
					}
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			try {
				wb.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return obj;
	}
}
