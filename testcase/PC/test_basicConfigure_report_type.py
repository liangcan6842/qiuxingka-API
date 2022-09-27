import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"
@allure.feature("基础配置-举报分类")
@allure.story("举报分类测试用例")
@allure.description("新增举报分类")
def test_1_add_report_type(get_token_fixture):
    """新增、修改举报分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "name": "92711举报分类" #举报分类名称
    }
    url = URL + "/v1/reportClass/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("基础配置-举报分类")
@allure.story("举报分类测试用例")
@allure.description("删除举报分类")
def test_3_delete_group_type(get_token_fixture):
    """删除举报分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [2]
    url = URL + "/v1/reportClass/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("基础配置-举报分类")
@allure.story("举报分类测试用例")
@allure.description("分页查询举报分类")
def test_4_pagination_query_report_type(get_token_fixture):
    """分页查询举报分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "name": 2,  #分类名称
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/reportClass/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()