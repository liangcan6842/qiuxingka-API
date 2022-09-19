import pytest,requests,json
URL = "http://192.168.110.244:8885"

def test_1_community_classity_add(get_token_fixture):
    """社区分类新增、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "status": 0, #状态,0:关闭,1:开启
            "name": "919测试社区"
    }
    url = URL + "/v1/dynamic/addColumn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_community_classity_select_page(get_token_fixture):
    """社区分类分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "page": 1,
            "limit": 10,
            "name": "919测试社区", #社区名称
            "startTime": "",
            "endTime": ""
    }
    url = URL + "/v1/dynamic/pageColumn"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_dynamic_list(get_token_fixture):
    """动态列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "page": 1,
            "limit": 10,
            "name": "", #用户昵称
            "startTime": "",
            "endTime": "",
            "state": "", #1：审核中；2：审核通过；3：审核不通过
            "status": "" #状态,0:关闭,1:开启
    }
    url = URL + "/v1/dynamic/pageDynamicList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


