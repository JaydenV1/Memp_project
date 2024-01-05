import os
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.comm_driver import CommDriver
from utils.handel_yml import get_yml_data
from utils.handel_path import config_path, screenshot_path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


'''
定义浏览器的基本操作
'''


class BasePage:
    def __init__(self):
        # 1 打开唯一浏览器,get_driver设置浏览器模式
        self.driver = CommDriver().get_driver(browser_name='chrome')
        # 2读取元素信息 进行动态获取属性
        self.locators = get_yml_data(os.path.join(config_path, 'all_elements.yaml'))[self.__class__.__name__]
        for k, v in self.locators.items():
            setattr(self, k, v)

    # 公共方法
    # 访问地址
    def open_url(self, url, page_load_time=20):
        # 设置一个页面加载超时时间
        self.driver.set_page_load_timeout(page_load_time)
        self.driver.get(url)

    # △△定位元素
    def get_element(self, locator, desc="定位错误"):
        # 通过显示等待定位元素，返回
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_element_located(locator))  # EC.visibility_of_element_located()方法表示需要等待直到元素可见
        except:
            # 截图 日志
            cur_time = time.strftime('%Y.%m.%d-%H%M%S')
            self.driver.get_screenshot_as_file(screenshot_path + f'Screenshot-{cur_time}.png')
            print(f'\n程序错误：未能定位到元素，请检查元素是否正确', f'\n截图路径：{screenshot_path}')
            return False

    def get_elements(self, locator, desc="定位错误"):
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_all_elements_located(locator))  # EC.visibility_of_element_located()方法表示需要等待直到元素可见
        except:
            # 截图 日志
            cur_time = time.strftime('%Y.%m.%d-%H%M%S')
            self.driver.get_screenshot_as_file(screenshot_path + f'Screenshot-{cur_time}.png')
            print(f'\n程序错误：未能定位到元素，请检查元素是否正确', f'\n截图路径：{screenshot_path}')
            return False

    # 输入操作
    def input_text(self, locator, text, desc=None):
        self.clean_text(locator)
        self.get_element(locator, desc=desc).send_keys(text)

    # 点击操作
    def click_element(self, locator):
        self.get_element(locator).click()

    def single_click(self, locator):
        ele = self.get_element(locator)
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()

    # 双击操作
    def double_click(self, locator):
        ActionChains(self.driver).double_click(locator).perform()
        ActionChains(self.driver).reset_actions()

    # 获取元素文本信息
    def get_element_text(self, locator):
        return self.get_element(locator).text

    def get_elements_text(self, locator):
        return [ele.text for ele in self.get_elements(locator)]

    # 清除文本内容
    def clean_text(self, locator):
        ele = self.get_element(locator)
        ele.clear()

    # 上传文件
    def upload_file(self, locator, path):
        self.driver.find_element(locator).send_keys(path)

    # 键盘enter按钮
    def keys_enter(self, locator):
        self.get_element(locator=locator).send_keys(Keys.ENTER)

    # 切换浏览器句柄
    def switch_handel(self):
        all_handel = self.driver.window_handles
        for i in all_handel:
            if self.driver.current_window_handle != i:
                self.driver.switch_to.window(i)

    # 退出操作
    def driver_quit(self):
        self.driver.quit()



if __name__ == '__main__':
    # print(BasePage().locators)
    pass
