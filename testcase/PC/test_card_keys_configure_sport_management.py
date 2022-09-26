import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_sport(get_token_fixture):
    """新增、修改运动"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "name": "924547348运动" #运动名称
    }
    url = URL + "/v1/cardMotion/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_sport(get_token_fixture):
    """删除运动"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [3]
    url = URL + "/v1/cardMotion/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_sport(get_token_fixture):
    """分页查询运动"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "name": 2,  #运动名称
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardMotion/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_sport_list(get_token_fixture):
    """运动列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "name": 2,  #运动名称
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardMotion/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200