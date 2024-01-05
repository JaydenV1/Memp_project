import unittest
import os
from BeautifulReport import BeautifulReport
import datetime

"""切换环境"""
# 使用哪个环境打开哪个环境
# 测试环境
# Environ = "/env_config/Offline/"
# 线上环境
Environ = "/env_config/Online/"


baseDir = os.path.dirname(__file__)
DIR = os.path.dirname(os.path.abspath(__file__))


def run(test_suite):
    # 测试报告：定义输出的文件位置和名字
    filename = "report.html"
    result = BeautifulReport(test_suite)
    result.report(filename=filename, description='便签项目接口测试报告', report_dir=DIR)


if __name__ == "__main__":

    # discover方法执行测试套件
    start_time = datetime.datetime.now()
    print("start time : {}".format(datetime.datetime.now()))
    case_level = "all"  # smoke 冒烟用例，all 全量用例
    if case_level == "smoke":
        pattern = "test_smoke*.py"
    else:
        pattern = "test_*.py"

    testsuite = unittest.defaultTestLoader.discover(
        start_dir=DIR + '/testCase',
        pattern=pattern
    )
    run(testsuite)
    end_time = datetime.datetime.now()
    print("end time : {}".format(end_time))
    print("use time : {}".format(end_time-start_time))


