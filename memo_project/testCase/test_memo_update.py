from Common.BaseApi import Request
from Common.handel_path import Test_config_path
from Common.handel_yaml import get_yaml
from parameterized import parameterized
import unittest


class TestMemoUpdate(unittest.TestCase):
    HOST = get_yaml(Test_config_path)['HOST']
    PATH = '/v3/notesvr/set/noteinfo'
    URL = HOST + PATH
    userid = get_yaml(Test_config_path)["userid"]

    @parameterized.expand([('001', 200), ('002', 200), ('003', 200)])
    def test_memo_update_001(self, num, code):
        """只传入正确的noteId"""
        body = {'noteId': num}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(code, resp.status_code)

    def test_memo_update_002(self):
        """传入空的请求头参数"""
        body = {'noteId': '001'}
        resp = Request.post_request(url=self.URL, body=body, userid=None)
        self.assertEqual(412, resp.status_code)

    def test_memo_update_003(self):
        """传入不正确的请求头参数"""
        body = {'noteId': '001'}
        resp = Request.post_request(url=self.URL, body=body, userid='127')
        self.assertEqual(412, resp.status_code)

    def test_memo_update_004(self):
        """传入不正确的noteId参数"""
        body = {'noteId': [1, 2, 3, 4]}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(500, resp.status_code)

    def test_memo_update_005(self):
        """传入空的noteId参数"""
        body = {'noteId': ''}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(500, resp.status_code)

    def test_memo_update_006(self):
        """传入start = 0（不标星）参数"""
        body = {'noteId': '001', 'star': 0}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(200, resp.status_code)

    def test_memo_update_007(self):
        """传入start = 1（标星）参数"""
        body = {'noteId': '001', 'star': 1}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(200, resp.status_code)

    def test_memo_update_008(self):
        """传入start 为空参数"""
        body = {'noteId': '001', 'star': ''}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(200, resp.status_code)

    def test_memo_update_009(self):
        """传入start 非int的参数"""
        body = {'noteId': '001', 'star': 'asd'}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(500, resp.status_code)

    def test_memo_update_010(self):
        """传入start 为布尔类型参数"""
        body = {'noteId': '001', 'star': True}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(500, resp.status_code)

    def test_memo_update_011(self):
        """传入remindTime为数字类型"""
        body = {'noteId': '001', 'star': 0, 'remindTime': 202312101212}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(200, resp.status_code)

    def test_memo_update_012(self):
        """传入remindTime为非数字类型"""
        body = {'noteId': '001', 'star': 0, 'remindTime': 'haha'}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(500, resp.status_code)

    def test_memo_update_013(self):
        """传入remindTime为空类型"""
        body = {'noteId': '001', 'star': 0, 'remindTime': ''}
        resp = Request.post_request(url=self.URL, body=body, userid=self.userid)
        self.assertEqual(200, resp.status_code)




