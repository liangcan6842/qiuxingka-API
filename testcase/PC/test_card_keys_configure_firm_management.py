import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_firm(get_token_fixture):
    """新增、修改厂商"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "name": "924厂商" #厂商名称
    }
    url = URL + "/v1/cardFirm/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_firm(get_token_fixture):
    """删除厂商"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [4]
    url = URL + "/v1/cardFirm/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_firm(get_token_fixture):
    """分页查询厂商"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "name": 2,  #厂商名称
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardFirm/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_firm_list(get_token_fixture):
    """厂商列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "name": 2,  #厂商名称
        # "status": 1,  #状态,0:关闭,1:开启
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/cardFirm/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200