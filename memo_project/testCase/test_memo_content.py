from Common.BaseApi import Request
from Common.handel_path import Test_config_path
from Common.handel_yaml import get_yaml, modify_yaml_file
from parameterized import parameterized
import unittest
import copy
global num


class TestMemoContent(unittest.TestCase):
    PATH = '/v3/notesvr/set/notecontent'
    HOST = get_yaml(Test_config_path)['HOST']
    URL = HOST + PATH
    userid = get_yaml(Test_config_path)["userid"]

    num = get_yaml(Test_config_path)["num"]
    body = {'noteId': '012',
            'title': 'just title',
            'summary': 'hhh',
            'body': 'content',
            'localContentVersion': num,
            'BodyType': '0'}

    def test_memo_content_001(self):
        """更新内容正向情况"""

        res = Request.post_request(url=self.URL, body=self.body, userid=self.userid)
        # self.num = self.num + 1
        # # 更新yaml里的参数
        # modify_yaml_file(Test_config_path, 'num', self.num)
        self.assertEqual(200, res.status_code)

    def test_memo_content_002(self):
        """输入noteId为空值"""
        new_body = copy.copy(self.body)
        new_body['noteId'] = ''
        # self.body['localContentVersion'] = self.num + 2
        res = Request.post_request(url=self.URL, body=new_body, userid=self.userid)
        self.assertEqual(500, res.status_code)

    def test_memo_content_003(self):
        """输入title为空值"""
        new_body1 = copy.copy(self.body)
        self.body['title'] = ''
        # self.body['localContentVersion'] = self.num + 1
        res = Request.post_request(url=self.URL, body=self.body, userid=self.userid)
        self.num = self.num + 1
        # 更新yaml里的参数
        modify_yaml_file(Test_config_path, 'num', self.num)
        self.assertEqual(200, res.status_code)

    def test_memo_content_004(self):
        """输入title为非字符串"""
        new_body = copy.copy(self.body)
        new_body['title'] = [1, 2, 3]
        # self.body['localContentVersion'] = self.num + 4
        res = Request.post_request(url=self.URL, body=new_body, userid=self.userid)
        self.assertEqual(500, res.status_code)

    def test_memo_content_005(self):
        """输入summary为空值"""
        # self.body['localContentVersion'] = self.num + 1
        res = Request.post_request(url=self.URL, body=self.body, userid=self.userid)
        self.num = self.num + 1
        # 更新yaml里的参数
        modify_yaml_file(Test_config_path, 'num', self.num)
        self.assertEqual(200, res.status_code)

    def test_memo_content_006(self):
        """输入summary为非字符串"""
        new_body = self.body
        new_body['summary'] = [1, 2, 3]
        res = Request.post_request(url=self.URL, body=new_body, userid=self.userid)
        self.assertEqual(500, res.status_code)

    @parameterized.expand([('string', 500), (None, 500), ({'key': 'value'}, 500)])
    def test_memo_content_007(self, value, code):
        """输入localContentVersion为非int类型"""
        new_body = self.body
        new_body['localContentVersion'] = value
        res = Request.post_request(url=self.URL, body=new_body, userid=self.userid)
        self.assertEqual(code, res.status_code)
