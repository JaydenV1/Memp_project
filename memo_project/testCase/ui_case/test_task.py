from Common.BaseApi import Request
from Common.handel_path import Test_config_path
from Common.handel_yaml import get_yaml, modify_yaml_file
from Common.handel_path import all_elements_path
from libs.ui_lib.login_page import LoginPage
from libs.ui_lib import movies_page, main_page
import unittest, time


class TestLogin(unittest.TestCase):
    HOST = get_yaml(all_elements_path)['DOUBANHOST']
    username = get_yaml(all_elements_path)['username']
    psw = get_yaml(all_elements_path)['psw']

    @classmethod
    def setUpClass(cls):
        LoginPage().open_login_page(cls.HOST).login(cls.username, cls.psw)
        time.sleep(3)
        account_name = LoginPage().get_account_name()
        cls.main_page = main_page.MainPage()

    def test_task001(self):
        """点击电影导航栏"""
        movie_page = self.main_page.movies_page()
        time.sleep(3)
        movie_title = movie_page.get_title()
        self.assertEqual('豆瓣电影', movie_title)





