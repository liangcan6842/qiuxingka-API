import pytest,requests,json
URL = "http://192.168.110.244:8885"
def test_1_add_user(get_token_fixture):
    """新增用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "username": "test1",
        "password": "123456",
        "nickName": "用户1",
        "avatar": "头像",
        "roleIds": [1]
    }
    url = URL + "/v1/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_select_user(get_token_fixture):
    """查询用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":"43"}
    url = URL + "/v1/view"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_select_user_list(get_token_fixture):
    """查询用户列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":"10",
        "page":"1",
        "username":"",
        "nickName":"",
        "status":"",
        "roleId":"",
        "roleName":"",
        "startTime":"",
        "endTime":""
    }
    url = URL + "/v1/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
