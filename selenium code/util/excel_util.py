#coding=utf-8
#操作Excel文件

import xlrd
#数据拿到copy一份，保留原数据
from xlutils.copy import copy
import time
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "/Users/pmy/Downloads/selenium code/config/casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        #拿到整个excel文件数据
        self.data = xlrd.open_workbook(self.excel_path)
        #拿到Excel中某一个sheet内容数据
        self.table = self.data.sheets()[index]      

    #目标返回list 数据格式：[[],[]]
    #获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []   #空字典
        #行数
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #获取excel行数
    def get_lines(self):
        #行数
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    #获取单元格的数据
    def get_col_value(self,row,col):
        #print 
        if self.get_lines()>row:
            #第几行第几列
            data = self.table.cell(row,col).value
            return data
        return None


    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)  #如果用self.data只能读取一条
        write_data = copy(read_value)
        #固定列数第10列
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
        time.sleep(1)


if __name__ == '__main__':
    ex = ExcelUtil('/Users/pmy/Downloads/selenium code/config/keyword.xls')
    print(ex.get_col_value(1,2))