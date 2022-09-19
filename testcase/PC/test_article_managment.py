import pytest,requests,json
URL = "http://192.168.110.244:8885"

def test_1_add_article(get_token_fixture):
    """文章新增、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,
        "title": "球星卡拍卖会",
        "synopsis": "球星卡大卖，单人、多人组团",   #简介
        "content": "球星卡内容",
        "coverImg": "C罗",
        "views": 20,
        "comments": 10,
        "likes": 100,
        "collects": 50
    }
    url = URL + "/v1/news/addColumn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_article_list(get_token_fixture):
    """文章列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "startTime": "",
        "endTime": "",
        "title": ""
    }
    url = URL + "/v1/news/newsList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_community_delete(get_token_fixture):
    """社区分类删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [1]
    url = URL + "/v1/news/newsList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



