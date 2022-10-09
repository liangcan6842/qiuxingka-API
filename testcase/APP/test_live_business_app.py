import requests,json,pytest,allure,os
URL = "http://192.168.110.173:8885"
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("直播设置")
def test_1_live_configure(get_token_fixture):
    """直播设置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "bookTime": "2022-10-09 14:08:35", #开始时间
        "descp": "开始直播" #直播描述
    }
    url = URL + "/v1/a/live/book"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("获取直播设置")
def test_2_get_live_configure(get_token_fixture):
    """获取直播设置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/live/book"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("开始直播")
def test_3_begin_live(get_token_fixture):
    """开始直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/live/start"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("结束直播")
def test_4_end_live(get_token_fixture):
    """结束直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/live/end"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("我的直播记录")
def test_5_my_live_record(get_token_fixture):
    """我的直播记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10,
        "page":1,
        # "state":1
    }
    url = URL + "/v1/a/live/my"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("录制直播")
def test_6_record_live(get_token_fixture):
    """录制直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "groupId": 3,
        "name": "录制直播"
    }
    url = URL + "/v1/a/live/record"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("结束录制直播")
def test_7_end_record_live(get_token_fixture):
    """结束录制直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "taskId": "" #录制id
    }
    url = URL + "/v1/a/live/stop"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("app直播测试")
@allure.story("app直播测试用例")
@allure.description("获取直播推流")
def test_8_get_live_flow(get_token_fixture):
    """获取直播推流"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/live/push"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()









