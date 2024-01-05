# handel_path
# 2022 / 3 / 27
# # =======
# Jayden

"""
自动化获得需要文件的路径，用这个脚本实现
"""
import os

# print(__file__)     #获取当前文件下的路径
# print(os.path.dirname(__file__))    #获取这个文件的上一层路径


# 获取项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # abspath:绝对路径
# print(project_path)
# 获取测试数据的路径
testdata_path = os.path.join(project_path, 'data/')
# print(testdata_path)
# 获取测试报告路径
report_path = os.path.join(project_path, r'outfile/report/tmp/')
# 获取配置数据的路径
config_path = os.path.join(project_path, 'Config/test_env/')
# 获取截图路径
screenshot_path = os.path.join(project_path, r'outfile/screenshot/')

print(config_path)
