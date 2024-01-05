import requests
from Common.handel_yaml import get_yaml
from Common.handel_path import Test_config_path
from Common.custom_log import info_log, error_log

TOKEN = get_yaml(Test_config_path)["TOKEN"]
userid = get_yaml(Test_config_path)["userid"]


class Request:
    @staticmethod
    def post_request(url, body, wps_sid=TOKEN, userid=userid):
        """

        :param userid:
        :param wps_sid:
        :param url: 输入URL
        :param body: 输入参数body，json格式
        :param token: 输入请求时需要的token，默认为万能token
        :return: 请求成功返回接口响应信息，请求失败会记录日志
        """
        header = {'Cookie': f'wps_sid={wps_sid}', 'X-user-key': userid}
        try:
            res = requests.post(url=url, headers=header, json=body)
            info_log(f'请求地址：{res.url}')
            info_log(f'接口状态码：{res.status_code}')
            info_log(f"接口请求文本：{res.request.body}")
            info_log(f"接口响应文本：{res.text}")
            return res
        except Exception as e:
            error_log(f'python执行的错误信息{e}')
            return e

    @staticmethod
    def get_request(url, wps_sid=TOKEN, body=None):
        header = {'Cookie': f'wps_sid={wps_sid}'}
        try:
            res = requests.get(url=url, headers=header, params=body)
            info_log(f'请求地址：{res.url}')
            info_log(f'接口状态码：{res.status_code}')
            info_log(f"接口响应文本：{res.text}")
            info_log(res.headers)
            return res
        except Exception as e:
            error_log(f'python执行的错误信息{e}')
            return e
