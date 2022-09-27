import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"
@allure.feature("消息中心")
@allure.story("后台消息测试用例")
@allure.description("标记已读")
def test_1_mark_read(get_token_fixture):
    """标记已读"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[]
    url = URL + "/v1/sysMessage/updateRead"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("消息中心")
@allure.story("后台消息测试用例")
@allure.description("删除消息")
def test_1_delete_message(get_token_fixture):
    """删除消息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[]
    url = URL + "/v1/sysMessage/del"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("消息中心")
@allure.story("后台消息测试用例")
@allure.description("分页查询消息")
def test_2_pagination_query(get_token_fixture):
    """分页查询消息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1
    }
    url = URL + "/v1/sysMessage"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()










