import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_post_order_shiped(get_token_fixture):
    """邮寄订单发货"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId": 1,  #订单id
        "courierNumber": "202209230957495299",  #快递单号
        "courierServicesCompany": "韵达快递"  #快递公司
    }
    url = URL + "/v1/mailingOrder/deliver"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_pc_pagination_query(get_token_fixture):
    """总后台分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "code": "202209230957495299",  #订单号
        "phone": "13212341234",  #用户手机号码
        "state": 0,  #
        "startTime": "",
        "endTime": ""
    }
    url = URL + "/v1/background/mailingOrder/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query(get_token_fixture):
    """分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "code": "202209230957495299",  #订单号
        "phone": "13212341234",  #用户手机号码
        "state": 0,  #0-待发货，1-待收货，2-已收货
        "startTime": "",
        "endTime": ""
    }
    url = URL + "/v1/mailingOrder/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_4_detail_query(get_token_fixture):
    """详情查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "camilleIds": "11,99,25" #订单卡密集合
    }
    url = URL + "/v1/mailingOrder/info"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_post_order_export(get_token_fixture):
    """邮寄订单导出"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "code": "202209230957495299",  #订单号
        "phone": "13212341234",  #用户手机号码
        "name": "球卡",  #商品名称
        "state": 1,  #状态：0-待发货，1-待收货，2-已收货
        "startTime": "",
        "endTime": ""
    }
    url = URL + "/v1/mailingOrder/export"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_pc_post_order_export(get_token_fixture):
    """总后台邮寄订单导出"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "code": "202209230957495299",  #订单号
        "phone": "13212341234",  #用户手机号码
        "name": "",  #商品名称
        "state": 0,  #0-待支付，1-已支付,2-待收货，3-已收货,4-已退款
        "startTime": "",
        "endTime": ""
    }
    url = URL + "/v1/background/mailingOrder/export"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



