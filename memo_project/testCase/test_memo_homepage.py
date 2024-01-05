from Common.BaseApi import Request
from Common.handel_path import Test_config_path
from Common.handel_yaml import get_yaml
import unittest


class TestGetHomePage(unittest.TestCase):
    HOST = get_yaml(Test_config_path)['HOST']
    PATH = '/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'

    def test_get_list_001(self):
        """
        输入userid、startindex、rows的参数都正确
        """
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', '10').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(200, resp.status_code)

    def test_get_list_002(self):
        """输入userid为空时"""
        new_path = self.PATH.replace('{userid}', '').replace('{startindex}', '10').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(404, resp.status_code)

    def test_get_list_003(self):
        """输入userid和cookie用户不一致时"""
        new_path = self.PATH.replace('{userid}', '001').replace('{startindex}', '10').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(412, resp.status_code)

    def test_get_list_004(self):
        """输入错误的userid参数类型"""
        new_path = self.PATH.replace('{userid}', 'suer').replace('{startindex}', '10').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(500, resp.status_code)

    def test_get_list_005(self):
        """输入空的startindex参数"""
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', '').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(404, resp.status_code)

    def test_get_list_006(self):
        """输入错误类型的startindex参数"""
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', 'hahaxi').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(500, resp.status_code)

    def test_get_list_007(self):
        """输入17位数字的startindex参数"""
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}',
                                                                      '123456789101231231233123').replace('{rows}',
                                                                                                          '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(500, resp.status_code)

    def test_get_list_008(self):
        """输入列表类型的startindex参数"""
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', '[1,2]').replace('{rows}', '10')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(500, resp.status_code)

    def test_get_list_009(self):
        """
        输入rows非数字类型
        """
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', '10').replace('{rows}', 'zing')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(500, resp.status_code)

    def test_get_list_0010(self):
        """
        输入rows为空
        """
        new_path = self.PATH.replace('{userid}', '567588558').replace('{startindex}', '10').replace('{rows}', '')
        url = self.HOST + new_path
        resp = Request.get_request(url=url)
        self.assertEqual(404, resp.status_code)
