"""
此文件相当于一个路径中转站，可以转移到不同的页面路径
"""
from Common.BaseUi import BasePage
from libs.ui_lib.movies_page import Moviespage
import time


class MainPage(BasePage):
    def movies_page(self):
        self.single_click(locator=self.movies_pages)
        time.sleep(3)
        self.switch_handel()
        return Moviespage()


