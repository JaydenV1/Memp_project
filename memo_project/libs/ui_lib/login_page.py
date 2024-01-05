from Common.BaseUi import BasePage
from libs.ui_lib.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains
from Common.handel_yaml import get_yaml
from Common.handel_path import all_elements_path
from selenium.webdriver.common.by import By
import cv2
import re
import requests
import time


class LoginPage(BasePage):

    def open_login_page(self, url):
        self.open_url(url)
        return self

    @staticmethod
    def get_pos(image):
        """计算验证图片缺口的x坐标"""
        # 首先使用高斯模糊去噪，噪声会影响边缘检测的准确性，因此首先要将噪声过滤掉
        blurred = cv2.GaussianBlur(image, (5, 5), 0, 0)

        # 边缘检测，得到图片轮廓
        canny = cv2.Canny(blurred, 200, 400)  # 200为最小阈值，400为最大阈值，可以修改阈值达到不同的效果

        # 轮廓检测
        # cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的，再转成二值图，此处canny已经是二值图
        # contours：所有的轮廓像素坐标数组，hierarchy 轮廓之间的层次关系
        contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours, hierarchy)

        for i, contour in enumerate(contours):  # 对所有轮廓进行遍历
            M = cv2.moments(contour)  # 并计算每一个轮廓的力矩(Moment)，就可以得出物体的质心位置
            # print(M)
            if M['m00'] == 0:
                cx = cy = 0
            else:
                # 得到质心位置，打印这个轮廓的面积和周长，用于过滤
                cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
                print(cv2.contourArea(contour), cv2.arcLength(contour, True))

            # 判断这个轮廓是否在这个面积和周长的范围内
            if 5000 < cv2.contourArea(contour) < 8000 and 300 < cv2.arcLength(contour, True) < 500:
                print(cx)
                if cx < 300:
                    continue
                print(cv2.contourArea(contour))
                print(cv2.arcLength(contour, True))

                # 外接矩形，x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 画出矩行
                # cv2.imshow('image', image)
                cv2.imwrite('111.jpg', image)  # 保存
                return x
        return 0

    def login(self, username, password):
        # 切换iframe
        iframe = self.get_element(self.iframe)
        self.driver.switch_to.frame(iframe)
        # 点击
        self.click_element(self.psw_login_button)
        # 输入用户名
        self.input_text(self.username_input, username)
        # 输入密码
        self.input_text(self.psw_input, password)
        # 登录
        ele = self.get_element(self.login_btn)
        self.click_element(self.login_btn)
        # self.driver.execute_script("arguments[0].click();", ele)

        # 出现滑块验证，出现新的iframe，这个iframe有id属性，直接使switch_to.frame('id值')
        self.driver.switch_to.frame(self.get_element(self.iframe_confirm))
        # 找到缺口验证码图片位置
        src = self.driver.find_element(by=By.XPATH, value='//*[@id="slideBg"]')
        style = src.get_attribute('style')
        # 通过正则表达式提取url中的地址
        compile_ = re.compile(r'background-image: url\("(.*?)"\)')
        png_address = re.findall(compile_, style)  # findall默认通过列表追加匹配到的数据
        print(png_address)

        # 保存图片
        url = png_address[0]
        req = requests.get(url=url)
        with open("./a.jpg", mode='wb') as file:
            file.write(req.content)

        # 读取图片
        verify_img = cv2.imread('a.jpg')
        # 调用函数，得到x坐标
        x = self.get_pos(verify_img)

        # 获取滑动条元素
        slide = self.driver.find_element(By.XPATH, '//*[@id="tcOperation"]/div[6]')

        # 图片实际像素与浏览器中图片像素有差异，浏览器中图片像素大概是实际图片的41%, 由于像素缩小，减去30像素是为了平滑距离
        result = int(x * 0.41) - 30

        # 滑动滑块
        ActionChains(self.driver).drag_and_drop_by_offset(slide, result, 0).perform()
        time.sleep(5)

    def get_account_name(self):
        return self.get_element_text(self.account_name)




if __name__ == '__main__':
    HOST = get_yaml(all_elements_path)['DOUBANHOST']
    username = get_yaml(all_elements_path)['username']
    psw = get_yaml(all_elements_path)['psw']
    # print(LoginPage().username_input)  # 这里因为使用了setattr
    LoginPage().open_login_page(HOST).login(username, psw)
    input()
    time.sleep(3)
    name = LoginPage().get_account_name()
    print(name)
    input()
    time.sleep(5)
    main_page = MainPage()
    movies_page = main_page.movies_page()
    movies_page.search_movies(movie_name='新闻女王')

    input('点击enter结束：')
    # FXO.driver_quit()
