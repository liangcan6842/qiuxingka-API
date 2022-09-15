import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_register(get_token_fixture):
    """注册"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "phone": "18875272518",
        "code": "12345678", #短信验证码
        "password": "123456",
        "wechatOpenid": "",
        "qqOpenid": "",
        "nickName": "",
        "headimg": ""    }
    url = URL + "/v1/a/user/register"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_get_user_message(get_token_fixture):
    """获取登录用户基本信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/getHomeUser"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_business_settled(get_token_fixture):
    """商家入驻"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,
        "userId": 7,
        "shopName": "",
        "areaCode": "",
        "area": "",
        "address": "",
        "headimg": "",
        "frontidcard": "",
        "backidcard": "",
        "business": "",
        "state": 0,          #1：审核中；2：已通过；3：已拒绝
        "checkUserId": 0,
        "checkTime": "",
        "remark": "",
        "reason": ""
    }
    url = ""
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_my_homePage(get_token_fixture):
    """我的主页"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/myHomePage"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()
