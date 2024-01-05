from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # => 引入Chrome的配置

'''
定义浏览器的驱动获取，并且是单例模式
'''


# 单例 为了保证对象是唯一的
class Single:
    def __new__(cls, *args, **kwargs):  # 在创建对象时，Python 会先调用 __new__() 方法来创建一个实例对象
        # 重写new方法
        if not hasattr(cls, '_instance'):  # hasattr(对象,属性或方法名),判断对象中是否有某个属性或某个方法,返回值是布尔型
            # 如果没有_instance属性 调用父类创建对象 给_instance类属性了--->_instance 是一个类属性，它用于存储类的单例实例
            cls._instance = super().__new__(cls)
        return cls._instance


class CommDriver(Single):
    """
    ch_options配置是为了无头浏览器能正常运行，防止被识别爬虫
    browser_name='headless'/'firefox'/'chrome'
    """
    driver = None

    def get_driver(self, browser_name='chrome'):
        if self.driver is None:
            if browser_name == 'headless':
                ch_options = Options()
                ch_options.add_argument("--window-size=1920,1080")  # 专门应对无头浏览器中不能最大化屏幕的方案
                ch_options.add_argument("--start-maximized")  # 浏览器最大化
                ch_options.add_argument('--headless')  # => 为Chrome配置无头模式
                ch_options.add_argument('--disable-gpu')  # 禁用GPU，防止无头模式出现莫名的BUG
                ch_options.add_argument('--no-sandbox')
                ch_options.add_argument('--disable-dev-shm-usage')
                ch_options.add_argument('log-level=3')
                ch_options.add_argument('--disable-blink-features=AutomationControlled')  # 谷歌浏览器去掉访问痕迹
                ch_options.add_argument(
                    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/100.0.4896.127 Safari/537.36")
                ch_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开启开发者模式
                ch_options.add_experimental_option('useAutomationExtension', False)
                self.driver = webdriver.Chrome(options=ch_options)  # 去掉options参数就是正常浏览器效果
                self.driver.maximize_window()
            elif browser_name == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_name == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise ValueError(f'Not support browser {browser_name}')
        self.driver.implicitly_wait(15)
        return self.driver


if __name__ == '__main__':
    CommDriver().get_driver()
    CommDriver().get_driver()