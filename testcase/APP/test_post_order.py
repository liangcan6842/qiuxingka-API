import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_post_order(get_token_fixture):
    """生成邮寄订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "address": "重庆市渝北区",
        "contact": "测试用户921", #用户名称
        "phone": "13212341234",
        "remark": "新增邮寄订单",
        "list": [
            {
                "businessId": 7, #商家id
                "camileIds": "11,99,25"  #卡密集合 逗号分隔 1，2，3
            }
        ]
    }
    url = URL + "/v1/mailingOrder"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_query_post_order(get_token_fixture):
    """查询邮寄订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId":0   #邮寄订单id
    }
    url = URL + "/v1/mailingOrder"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_delete_post_order(get_token_fixture):
    """删除邮寄订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId":0   #邮寄订单id
    }
    url = URL + "/v1/mailingOrder/del"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_alter_post_order_state(get_token_fixture):
    """修改邮寄订单状态:确认收货"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId":0,   #邮寄订单id
        "state":0   #状态：0-待发货，1-待收货，2-已收货
    }
    url = URL + "/v1/mailingOrder/del"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
















