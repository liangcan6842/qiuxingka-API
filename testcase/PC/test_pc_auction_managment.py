import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_select_auction_product_order(get_token_fixture):
    """查询拍卖产品订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "auctionProductId": 2
    }
    url = URL + "/v1/auctionProduct/background/auctionOrder"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_2_select_auction_product_detail(get_token_fixture):
    """查询拍卖产品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "auctionProductId": 2
    }
    url = URL + "/v1/auctionProduct/background/details"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_3_seller_ship(get_token_fixture):
    """卖家发货"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "orderId": 14, #订单id
        "courierNumber": "202209221343567", #快递单号
        "courierServicesCompany": "顺丰快递" #快递公司
    }
    url = URL + "/v1/auctionProduct/deliverGoods"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_select_page(get_token_fixture):
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
            "name": "",
            "nickName": "" #手机号
            # "state":  #拍卖产品状态：0-下架，1-待拍卖，2-拍卖中，3-待支付，4-待发货，5待收货，6-已收货
    }
    url = URL + "/v1/auctionProduct/background/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_5_margin_pay_record(get_token_fixture):
    """保证金缴纳记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit": 10,
            "page": 1,
            "productionId": 2
    }
    url = URL + "/v1/auctionProduct/background/earnestMoney/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_bargain_record_detail(get_token_fixture):
    """议价记录详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "auctionProductionId": 2,
            "fromUserId": 8
    }
    url = URL + "/v1/auctionProduct/background/negotiated"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_7_bargain_record_page(get_token_fixture):
    """议价记录分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "productionId": 2,  #拍卖产品id
            "page": 1,
            "limit": 10
    }
    url = URL + "/v1/auctionProduct/background/negotiated/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_8_bid_record(get_token_fixture):
    """出价记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "productionId": 3,  #拍卖产品id
            "page": 1,
            "limit": 10
    }
    url = URL + "/v1/auctionProduct/background/bidding/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_9_bid_record_detail(get_token_fixture):
    """出价记录详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "biddingId": 2  #拍卖产品id
    }
    url = URL + "/v1/auctionProduct/background/bidding"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_10_cancel_audit(get_token_fixture):
    """取消审核"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 0, #审核数据id
        "state": 0, #审核状态 1-通过，0-不通过
        "remark": ""
    }
    url = URL + "/v1/auctionProduct/background/cancelCheck"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_11_cancel_audit_list(get_token_fixture):
    """取消审核列表"""
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
            "name": "",
            "nickName": "" #手机号
            # "state":  #拍卖产品状态：0-下架，1-待拍卖，2-拍卖中，3-待支付，4-待发货，5待收货，6-已收货
    }
    url = URL + "/v1/auctionProduct/background/cancelCheck/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_12_cancel_audit_detail(get_token_fixture):
    """取消审核详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "cancelCheckId": 1
    }
    url = URL + "/v1/auctionProduct/background/cancelCheck/details"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200