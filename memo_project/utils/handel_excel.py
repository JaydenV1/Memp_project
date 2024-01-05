# handel_Excel - Version3.py
# 2022 / 2 / 26
# # =======
# Jayden


# handel_Excel - Version2.py
# 2022 / 1 / 24
# # =======
# Jayden
'''
1.可以实现在excel拿特定的用例数据测试
2.可以实现自动化拿excel特定列的数据
'''
import xlrd
from xlutils.copy import copy
import json
import os
from utils.handel_path import testdata_path
from libs.api_lib.flex_trade import FixTrade_Controller
from libs.api_lib.fx_option_trade import FX_Option_Trade_Listing


def get_excel_data(sheetname,casename,*args,runcase=['all'],excelname='Flex trade data.xls'): #*args---封装元组
    '''
    :param excelname: excel的文件名
    :param sheetname: excel需要的表名
    :param casename: 需要的用例编号
    :param args:    获取需要列的数据
    :param runcase: 需要执行的用例
    :return:    格式：[(),()]
    '''

    excelpath = os.path.join(testdata_path,excelname)

    # 1- 打开一个文件  磁盘-读取-内存(对象--需要一个变量存储)
    workbook = xlrd.open_workbook(excelpath,formatting_info=True)   #formatting_info = True  保持原样式  颜色  字体
    # print(workbook.sheet_names())

    # 2- 使用表名获取对应的表
    worksheet = workbook.sheet_by_name(sheetname)

    #print(worksheet.col_values(0))
    #print(worksheet.row_values(0))
    #print(worksheet.cell_value(0,0))

    #3.列名转化为下标
    #args==['请求参数'，'响应的预期结果']
    excel_colid = []  # 定义空列表>>>为了储存获得的下标
    for one in args:    #遍历了需要的col
        excel_colid.append(worksheet.row_values(0).index(one))  #把取得的下标放入列表中
    #print('列的下标>>',excel_colid)

    #4.做用例筛选
    runlist = []                #里面存的是需要跑得用例编号
    num = worksheet.row_values(0).index('Jira')     #索引出所属的列数
    for one in runcase:         #先遍历需要跑的用例数字
        if 'all' in one:
            runlist = worksheet.col_values(num)
        else:
            if '-' in one:
                start,end = one.split('-')
                for i in range(int(start),int(end)+1):
                    casenames = f'{casename}{i:0>3}'
                    runlist.append(casenames)
            else:
                runlist.append(f'{casename}{one:0>3}')
    # print(runlist)



    # 5- 获取需要的 数据
    rowid = 0
    expect_list=[]
    num = worksheet.row_values(0).index('Jira')     #索引出所属的列数
    for i in worksheet.col_values(num):   #用i遍历excel的'Jira'列
        if casename in i and i in runlist:
            getcoldata = []             #具体列的数据
            for num in excel_colid:   #遍历下标的值
                tmp=is_json(worksheet.cell_value(rowid, num))
                getcoldata.append(tmp)
            #print(getcoldata)
            expect_list.append( tuple(getcoldata) )
        rowid += 1      #如果casename不符合rowid也是需要+1
    # print('数据:',expect_list)
    return expect_list

    #6.json判断是否需要转化成字典
def is_json(instr):
    try:
       return json.loads(instr)     #如果不报错就可以转字典
    except:
        return instr                #如果报错的话就返回原来的格式



def flex_data_conversion(sheetname,column):
    '''
此函数是把Flex_trade的请求数据按一定的格式剖析写进excel中，至于具体的格式是函数"FixTrade_Controller.data_analysis"决定
    :param sheetname: excel里的sheet
    :param column: 需要拿列的数据
    :return: 自动把读取的数据解析到"预期结果"中
    '''
    excelpath = os.path.join(testdata_path,'Flex trade data.xls')   #读取这个excel文件
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # formatting_info = True  保持原样式  颜色  字体
    worksheet = workbook.sheet_by_name(sheetname)        #获取sheet内容
    colnum = worksheet.row_values(0).index(column)     #索引出所属的列数
    # print(colnum)
    row = worksheet.col_values(0)
    newWb = copy(workbook)
    for rownum in range(1,len(row)):     #遍历有多少行
        #print(rownum)
        data = eval(worksheet.cell_value(rownum,colnum))    #eval():把字符串形式的列表，转换为列表
        #print(data,type(data))
        news = newWb.get_sheet('Jayden')
        news.write(rownum,colnum+1,FixTrade_Controller.data_analysis(data))     #在某行某列按某格式写进excel
        newWb.save(testdata_path+"/flex data(conversion).xls")

def Fx_option_data_conversion(sheetname,column):
    '''
此函数是把Flex_trade的请求数据按一定的格式剖析写进excel中，至于具体的格式是函数"FixTrade_Controller.data_analysis"决定
    :param sheetname: excel里的sheet
    :param column: 需要拿列的数据
    :return: 自动把读取的数据解析到"预期结果"中
    '''
    excelpath = os.path.join(testdata_path,'Flex trade data.xls')   #读取这个excel文件
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # formatting_info = True  保持原样式  颜色  字体
    worksheet = workbook.sheet_by_name(sheetname)        #获取sheet内容
    column = worksheet.row_values(0).index(column)     #索引出所属的列数
    # print(column)
    row = worksheet.col_values(0)
    newWb = copy(workbook)
    for row_num in range(1,len(row)):     #遍历有多少行
        #print(row_num)
        global null,true,false
        null =""
        true = True
        false = False
        try:
            data = eval(worksheet.cell_value(row_num,column))    #eval():把字符串形式的列表，转换为列表
        except:
            pass
        #print(data,type(data))
        news = newWb.get_sheet('FX_Option')
        news.write(row_num,column+1,FX_Option_Trade_Listing.data_analysis(playload=data))     #在某行某列按某格式写进excel
        newWb.save(testdata_path+"/flex data(conversion).xls")


if __name__ == '__main__':
    # get_excel_data('Jayden','FOIB',*['步骤描述','预期结果','用例名称'],excelname='flex data(conversion).xls')
    Fx_option_data_conversion('FX_Option', '请求参数')
    get_excel_data('FX_Option', 'FOIB-', *['用例名称', '请求参数', '预期结果'],runcase=['001'],excelname='flex data(conversion).xls')