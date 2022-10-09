import requests,json,pytest,allure,os
URL = "http://192.168.110.173:8885"
@allure.feature("直播管理")
@allure.story("直播管理测试用例")
@allure.description("关闭直播")
def test_1_close_live(get_token_fixture):
    """关闭直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "roomId": 2,
        "expired": "2022-10-09 15:51:16", #恢复时间
        "reason": "违反直播规则"
    }
    url = URL + "/v1/live/stop"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("直播管理")
@allure.story("直播管理测试用例")
@allure.description("恢复直播")
def test_2_recover_live(get_token_fixture):
    """恢复直播"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "roomId":2
    }
    url = URL + "/v1/live/resume"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("直播管理")
@allure.story("直播管理测试用例")
@allure.description("查询直播间")
def test_3_query_live_room(get_token_fixture):
    """查询直播间"""
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
    url = URL + "/v1/live/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()









