import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_alter_user_disable_information(get_token_fixture):
    """修改用户禁用信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "status": 0, #状态,0:关闭,1:开启
            "userId": 0,
            "loginDisable": 0, #登录是否禁用（1：正常；2：禁用有期限；3：永久禁用）
            "loginDays": 0,
            "loginExpireTime": "",
            "chatDisable": 0,   #聊天是否禁用（1：正常；2：禁用有期限；3：永久禁用）
            "chatDays": 0,
            "chatExpireTime": "",
            "dynamicDisable": 0,  #发布动态是否禁用（1：正常；2：禁用有期限；3：永久禁用）
            "dynamicDays": 0,
            "dynamicExpireTime": "" #禁用到期日期
    }
    url = URL + "/v1/webUser/updateUserDisable"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_user_list(get_token_fixture):
    """查询用户列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        "startTime": "",
        "endTime": "",
        "nickName": "",
        "disable": ""
    }
    url = URL + "/v1/webUser/userList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_user_details(get_token_fixture):
    """查询用户详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data ={ "id":"7"}
    url = URL + "/v1/webUser/userDetails"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_user_disable_details_information(get_token_fixture):
    """用户禁用详情信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/webUser/userDisableDetails"
    data ={ "id":"1"}
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()
