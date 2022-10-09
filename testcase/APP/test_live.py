import requests,json,pytest,allure,os
URL = "http://192.168.110.173:8885"
@allure.feature("app直播")
@allure.story("app直播测试用例")
@allure.description("直播点赞")
def test_1_live_like(get_token_fixture):
    """直播点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 2, #房间id
        "count": 1314
    }
    url = URL + "/v1/a/live/normal/like"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_2_query_live_room(get_token_fixture):
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
    url = URL + "/v1/a/live/normal/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200