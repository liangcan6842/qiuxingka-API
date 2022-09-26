import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_series(get_token_fixture):
    """新增、修改系列"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 3, #修改必传
        "name": "924系列", #系列名称
        "seasonId": 2, #赛季id
        "motionId": 2, #运动id
        "firmId": 3 #厂商id
    }
    url = URL + "/v1/cardSeries/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_series(get_token_fixture):
    """删除系列"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [4]
    url = URL + "/v1/cardSeries/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_series(get_token_fixture):
    """分页查询系列"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "name": 2,  #系列名称
        # "seasonId": 0,  # 赛季id
        # "motionId": 0,  # 运动id
        # "firmId": 0  # 厂商id
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardSeries/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_not_pagination_query_series(get_token_fixture):
    """未分页查询系列"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "name": 2,  #系列名称
        # "seasonId": 0,  # 赛季id
        # "motionId": 0,  # 运动id
        # "firmId": 0  # 厂商id
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardSeries/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200