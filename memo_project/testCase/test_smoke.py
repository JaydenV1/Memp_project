import unittest
from Common.handel_path import project_path
import os
from testCase.test_memo_homepage import TestGetHomePage
import testCase.test_memo_homepage, test_memo_update, test_memo_content

# 按文件路径加载用例
# file_path = os.path.join(project_path, r"testCase")
# suit = unittest.TestLoader().discover('./', 'test_memo_content.py')
# runner = unittest.TextTestRunner()
# runner.run(suit)    # 使用run方法运行测试套件


# 按测试套件运行用例
suit = unittest.TestSuite()
loader = unittest.TestLoader()  # 创建加载器对象
# suit.addTest(loader.loadTestsFromTestCase(testCaseClass=TestGetHomePage))  # 通过测试类加载测试
# suit.addTest(loader.loadTestsFromModule(testCase.test_memo_homepage))        # 通过模块名添加该模块内所有的测试用例
suit.addTest(loader.loadTestsFromNames(['testCase.test_memo_homepage', 'testCase.test_memo_update']))
# 根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名
runner = unittest.TextTestRunner()
# 使用run方法运行测试套件
runner.run(suit)
