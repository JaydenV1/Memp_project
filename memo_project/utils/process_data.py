# process_data
# 2022 / 5 / 3
# # =======
# Jayden
import xlrd,xlwt
from xlutils.copy import copy
import os
from utils.handel_path import testdata_path


# def process_data(sheetname,casename,*args,runcase=['all'],excelpath='Flex trade data.xls'):
    # excel处理
excelpath = os.path.join(testdata_path, 'Flex trade data.xls')
workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # formatting_info = True  保持原样式  颜色  字体
newWb = copy(workbook)
news = newWb.get_sheet('Jayden')

    #获取数据下标
xlwt.Row
print(num)

    # news.write(16, 16, 内容)      #处理逻辑点
    #
    #
    #
    # newWb.save(testdata_path + "/flex data.xls")