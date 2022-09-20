import pytest
import requests
import json
URL = "http://192.168.110.173:8885"

@pytest.fixture(scope="session")
def get_token_fixture():
    '''
    作用域为session的fixture函数，返回token
    :return:
    '''
    headers = {"Content-Type": "application/json;charset=utf8"}
    url = URL + "/v1/a/login"
    data = {
            "type": 1, #1密码登录；2 短信验证码登录
            "phone": "18875272518",
           # "code": "123456", #短信验证码
            "password": "123456"
    }
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    token = res["data"]
    return token