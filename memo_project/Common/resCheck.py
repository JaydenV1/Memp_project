import unittest


class ResCheck(unittest.TestCase):
    def res_check(self, expected_body, response):
        """
        expected_body: {"key": type}
        response: dict
        校验http接口返回值校验
        :key: is exist.
        :value type: true or false.
        :len(key): actual true.
        """
        self.assertEqual(len(expected_body.keys()), len(response.keys()))
        for k, v in expected_body.items():
            self.assertIn(k, response.keys())
            self.assertEqual(v, type(response[k]))

    def res_all_check(self, expected_body, response):
        """
        校验http接口返回值校验
        expected_body: {"key": "value"}
        response: dict
        :key: is exist.
        :value type: true or false.
        :len(key): actual true.
        """
        self.assertEqual(len(expected_body.keys()), len(response.keys()))
        for k, v in expected_body.items():
            self.assertIn(k, response.keys())
            self.assertEqual(type(v), type(response[k]))
            self.assertEqual(v, response[k])
