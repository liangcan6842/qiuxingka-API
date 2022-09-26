import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_seller_shiped(get_token_fixture):
    """卖家发货"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId": 3,  #订单id
        "courierNumber": "",  #快递单号
        "courierServicesCompany": ""  #快递公司
    }
    url = URL + "/v1/merchant/orderList/deliverGoods"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_pagination_query(get_token_fixture):
    """分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "startTime": "",
        "endTime": "",
        "order": "",  #订单名称
        "phone": "",  #买家手机号码
        "name": "",  #商品名称
        "state": "",  #0-待支付，1-已支付,2-待收货，3-已收货,4-已退款
        "orderType": "",  #订单类型 1-保证金，2-一口价，3-竞价，4-议价
        "nickName": ""  #买家昵称
    }
    url = URL + "/v1/merchant/auctionOrder/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_order_export(get_token_fixture):
    """订单导出"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "startTime": "",
        "endTime": "",
        "order": "",  #订单名称
        "phone": "",  #买家手机号码
        "name": "",  #商品名称
        "state": "",  #0-待支付，1-已支付,2-待收货，3-已收货,4-已退款
        "orderType": "",  #订单类型 1-保证金，2-一口价，3-竞价，4-议价
        "nickName": ""  #买家昵称
    }
    url = URL + "/v1/merchant/auctionOrder/export"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200