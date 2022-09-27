import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_open_card_time(get_token_fixture):
    """新增、修改开卡时间"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "num": 9 #时间数
    }
    url = URL + "/v1/productTimes/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_add_sale_cycle(get_token_fixture):
    """新增、修改销售周期"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 0, #修改必传
        "num": 2 #时间数
    }
    url = URL + "/v1/productTimes/addSalesCycle"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_delete_open_time(get_token_fixture):
    """删除开卡时间"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = []
    url = URL + "/v1/productTimes/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_pagination_query_open_time(get_token_fixture):
    """分页查询开卡时间、周期"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "type": 2,  #	1：销售周期；2：开卡时间
        "startTime": "",
        "endTime": ""
    }
    url = URL + "/v1/productTimes/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_not_pagination_list(get_token_fixture):
    """未分页列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "type": 2  #	1：销售周期；2：开卡时间
    }
    url = URL + "/v1/productTimes/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
