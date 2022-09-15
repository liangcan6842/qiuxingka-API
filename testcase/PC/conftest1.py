import pytest
import requests
import json
import yaml

yaml_path = "C:\\Users\\Administrator\\Desktop\\捷成接口测试\\data\\login.yml"
def read_yaml(yaml_path):
    with open(yaml_path,'r',encoding='utf-8') as yml:
        yml_data = yaml.load(yml,yaml.FullLoader)
    return yml_data


#
# @pytest.fixture(scope="session")
# def get_token_fixture():
#     '''
#     作用域为session的fixture函数，返回token
#     :return:
#     '''
#     headers = {"Content-Type": "application/json;charset=utf8"}
#     data = {
#         "username": "admin",
#         "password": "123456"
#     }
#     res = requests.post(url=url, headers=headers, json=data).text
#     res = json.loads(res)
#     token = res["data"]
#     return token