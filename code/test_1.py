# coding:utf-8
 
import unittest
from dm_app_0 import app
import json
 
 
class TestLogin(unittest.TestCase):
    """定义测试案例"""
    
    # 测试代码执行之前调用 (方法名固定)
    def setUp(self):
        """在执行具体的测试方法前，先被调用"""
        # 可以使用python的http标准客户端进行测试
        # urllib  urllib2  requests
 
        # app.config['TESTING'] = True  # 指定app在测试模式下运行
        app.testing = True   # 指定app在测试模式下运行。 (测试模式下,视图中的意外异常可以正常打印显示出来)
        # 使用flask提供的测试客户端进行测试 (Flask客户端可以模拟发送请求)
        self.client = app.test_client()
    
    # 测试代码。 (方法名必须以"test_"开头)
    def test_empty_name_password(self):
        """测试模拟场景，用户名或密码不完整"""
        # 使用Flask客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/dologin", data={})
 
        # respoonse.data是响应体数据
        resp_json = response.data
 
        # 按照json解析
        resp_dict = json.loads(resp_json)
 
        # 使用断言进行验证
        self.assertIn("code", resp_dict)
 
        code = resp_dict.get("code")
        self.assertEqual(code, 1)
 
        # 测试只传name
        response = self.client.post("/dologin", data={"name": "admin"})
 
        # respoonse.data是响应体数据
        resp_json = response.data
 
        # 按照json解析
        resp_dict = json.loads(resp_json)
 
        # 使用断言进行验证
        self.assertIn("code", resp_dict)
 
        code = resp_dict.get("code")
        self.assertEqual(code, 1)
 
 
    # 测试代码。 (方法名必须以"test_"开头)
    def test_wrong_name_password(self):
        """测试用户名或密码错误"""
        
        response = self.client.post("/dologin", data={"name": "admin", "password": "xxx"})
 
        # respoonse.data是响应体数据
        resp_json = response.data
 
        # 按照json解析
        resp_dict = json.loads(resp_json)
 
        # 使用断言进行验证
        self.assertIn("code", resp_dict)
 
        code = resp_dict.get("code")
        self.assertEqual(code, 2)
 
 
if __name__ == '__main__':
    unittest.main()  # 进行测试